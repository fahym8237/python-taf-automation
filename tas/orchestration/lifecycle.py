

from __future__ import annotations

import hashlib
import traceback
from pathlib import Path
from typing import Optional

from tas.orchestration.parallel import get_worker_id, new_run_id
from tas.orchestration.artifacts import ArtifactManager
from tas.orchestration.logging import JsonlLogger, LogContext
from tas.orchestration.runner_context import RunContext, ScenarioContext
from tas.orchestration.tag_interpreter import TagInterpreter

from tas.config.loader import load_config

from tas.interaction.ui.ui_session import UiSession, UiSessionConfig
from tas.interaction.api.api_session import ApiSession, ApiSessionConfig

from pathlib import Path
from tas.observability.run_meta import write_run_meta, write_environment_properties


from tas.observability.attachments import Attachment, write_attachments_index

from tas.observability.exporters.traceability_csv import append_traceability_row

from tas.observability.attachments import Attachment, write_attachments_index
from tas.core.util.jsonutil import dumps_pretty
from tas.core.util.files import write_text

from tas.observability.exporters.allure_adapter import attach_file_if_possible, attach_text_if_possible
from tas.observability.trace_tags import extract_requirements

class LifecycleManager:
    

    def __init__(self) -> None:
        self._tag_interpreter = TagInterpreter()

    # ----------------------------
    # Behave hooks
    # ----------------------------
    def before_all(self, behave_context) -> None:
        worker_id = get_worker_id()
        run_id = new_run_id()

        # Load config BEFORE run_ctx exists (must not reference behave_context.run_ctx)
        cfg = load_config(behave_context)

        # Artifact manager rooted at configured artifact root
        artifact_root: Path = cfg.exec.artifact_root
        am = ArtifactManager(artifact_root)
        run_root = am.ensure_run_root(run_id, worker_id)

        # Run logger
        run_log = run_root / "run.log.jsonl"
        logger = JsonlLogger(run_log, LogContext(run_id=run_id, worker_id=worker_id))
        logger.info("run_started")

        

        # write run metadata
        write_run_meta(run_root, run_id, worker_id)

        # optional allure results dir
        allure_results_dir = Path("target/allure-results")
        allure_results_dir.mkdir(parents=True, exist_ok=True)

        write_environment_properties(allure_results_dir, {
            "browser": getattr(cfg.ui, "browser", ""),
            "headless": getattr(cfg.ui, "headless", ""),
            "trace_mode": getattr(cfg.ui, "trace_mode", ""),
            "api_base_url": getattr(cfg.api, "base_url", ""),
            "run_id": run_id,
            "worker_id": worker_id,
        })

        # Set run context
        behave_context.run_ctx = RunContext(
            run_id=run_id,
            worker_id=worker_id,
            run_root=run_root,
            logger=logger,
            services={
                "artifact_manager": am,
                "config": cfg,
                "allure_dir": allure_results_dir,
            },
        )
        

    def before_scenario(self, behave_context, scenario) -> None:
        if not hasattr(behave_context, "run_ctx"):
            raise RuntimeError("run_ctx not initialized. Check features/environment.py before_all.")

        run_ctx: RunContext = behave_context.run_ctx
        cfg = run_ctx.services.get("config")
        if cfg is None:
            raise RuntimeError("Config missing from run_ctx.services['config']. Check before_all stores it.")

        am: ArtifactManager = run_ctx.services["artifact_manager"]

        scenario_id = self._make_scenario_id(scenario.feature.name, scenario.name)
        scenario_root = am.ensure_scenario_root(run_ctx.run_root, scenario_id)

        tags = self._tag_interpreter.interpret(scenario.feature, scenario)

        # Scenario logger
        scenelog_path = scenario_root / "scenario.log.jsonl"
        scenelog = JsonlLogger(
            scenelog_path,
            LogContext(
                run_id=run_ctx.run_id,
                worker_id=run_ctx.worker_id,
                scenario_id=scenario_id,
                feature=scenario.feature.name,
                scenario=scenario.name,
            ),
        )
        scenelog.info("scenario_started", tags=sorted(list(tags.raw)))

        # ✅ Create scenectx FIRST (so it's always defined from here onward)
        scenectx = ScenarioContext(
            scenario_id=scenario_id,
            scenario_root=scenario_root,
            tags=tags,
            logger=scenelog,
        )
        behave_context.scenario_ctx = scenectx

        trace = extract_requirements(tags.raw)
        scenectx.set_service("trace", trace)

        if trace.requirement_ids:
            attach_text_if_possible("requirements", ", ".join(trace.requirement_ids))

        # ✅ Layer 8: per-scenario data bag
        scenectx.set_service("data", {})

        # ----------------------------
        # Start UI session if needed
        # ----------------------------
        if tags.is_ui or tags.is_hybrid:
            browser = tags.browser or cfg.ui.browser
            headless = cfg.ui.headless
            trace_mode = cfg.ui.trace_mode

            # Enforce UI URLs here (not in before_all)
            if not (cfg.ui_pilot.login_url and cfg.ui_pilot.forgot_url and cfg.ui_pilot.register_url):
                raise RuntimeError(
                    "Missing UI pilot URLs for @ui/@hybrid scenario. Provide:\n"
                    "  -D login_url=file:///.../login.html\n"
                    "  -D forgot_url=file:///.../forgot-password.html\n"
                    "  -D register_url=file:///.../register.html\n"
                    "or set env LOGIN_URL/FORGOT_URL/REGISTER_URL."
                )

            ui = UiSession(
                UiSessionConfig(
                    browser=browser,
                    headless=headless,
                    trace_mode=trace_mode,
                    artifacts_dir=scenario_root,
                )
            )
            ui.start()
            scenectx.set_service("ui", ui)
            scenelog.info("ui_session_started", browser=browser, headless=headless, trace_mode=trace_mode)  

        if tags.is_api or tags.is_hybrid:
            # Prefer Layer 7 config via -D api_base_url=..., fallback to env
            import os
            api_base_url = (cfg.api.base_url or "").strip()
            if not api_base_url:
                api_base_url = os.getenv("API_BASE_URL", "").strip()

            if not api_base_url:
                raise RuntimeError(
                    "Missing API base url. Provide one of:\n"
                    "  - Behave user-data: -D api_base_url=https://...\n"
                    "  - Environment: API_BASE_URL=https://..."
                )

            timeout_ms = int(getattr(cfg.api, "timeout_ms", 30000))

            api = ApiSession(
                ApiSessionConfig(
                    base_url=api_base_url,
                    timeout_ms=cfg.api.timeout_ms,
                    default_headers=cfg.api.default_headers,
                    ignore_https_errors=cfg.api.ignore_https_errors,  # ✅ critical
                )
            )
            api.start()
            scenectx.set_service("api", api)
            scenelog.info(
                "api_session_started",
                base_url=api_base_url,
                timeout_ms=cfg.api.timeout_ms,
                ignore_https_errors=cfg.api.ignore_https_errors,     # ✅ log it to verify
            )

        # ----------------------------
        # Start API session if needed (kept env-based until we extend config for API)
        # ----------------------------
        trace = extract_requirements(tags.raw)
        scenelog.info("traceability", requirements=trace.requirement_ids)
        scenectx.set_service("trace", trace)


    def after_step(self, behave_context, step) -> None:
        if not hasattr(behave_context, "scenario_ctx"):
            return

        scenectx: ScenarioContext = behave_context.scenario_ctx
        scenectx.logger._ctx.step = step.name  # correlation context

        if step.status == "failed":
            scenectx.logger.error("step_failed", step=step.name)

            items = []
            ui = scenectx.get_service("ui")
            if ui:
                png = scenectx.scenario_root / "failure_screenshot.png"
                # (already created in your current code; keep creating it)
                ui.screenshot(png)
                items.append(Attachment(name="failure_screenshot", path=str(png), mime="image/png"))
                #attach_file_if_possible("failure_screenshot", png, "image/png")
                attach_file_if_possible("failure_screenshot", png)

                trace_mode = behave_context.run_ctx.services["config"].ui.trace_mode
                if trace_mode in ("on-failure", "always"):
                    trace = scenectx.scenario_root / "trace.zip"
                    ui.stop_trace(trace)
                    items.append(Attachment(name="playwright_trace", path=str(trace), mime="application/zip"))
                    #attach_file_if_possible("playwright_trace", trace, "application/zip")
                    attach_file_if_possible("playwright_trace", trace)

            write_attachments_index(scenectx.scenario_root, items)

            api = scenectx.get_service("api")
            items = []
            if api and getattr(api, "last_exchange", None):
                ex = api.last_exchange
                req_path = scenectx.scenario_root / "api_last_request.json"
                resp_path = scenectx.scenario_root / "api_last_response.json"

                write_text(req_path, dumps_pretty({
                    "method": ex.method,
                    "url": ex.url,
                    "headers": ex.request_headers,
                    "json": ex.request_json,
                }))
                write_text(resp_path, dumps_pretty({
                    "status": ex.status,
                    "headers": ex.response_headers,
                    "json": ex.response_json,
                    "text": ex.response_text,
                }))

                items.append(Attachment(name="api_last_request", path=str(req_path), mime="application/json"))
                items.append(Attachment(name="api_last_response", path=str(resp_path), mime="application/json"))
                attach_file_if_possible("api_last_request", req_path)
                attach_file_if_possible("api_last_response", resp_path)
            write_attachments_index(scenectx.scenario_root, items)


    def after_scenario(self, behave_context, scenario) -> None:
        if not hasattr(behave_context, "scenario_ctx"):
            return

        scenectx: ScenarioContext = behave_context.scenario_ctx

        try:
            scenectx.cleanup()
        finally:
            # Close API session
            api = scenectx.get_service("api")
            if api:
                try:
                    api.close()
                finally:
                    scenectx.logger.info("api_session_closed")

            # Close UI session (save trace if always)
            ui: Optional[UiSession] = scenectx.get_service("ui")
            if ui:
                trace_mode = behave_context.run_ctx.services["config"].ui.trace_mode
                if trace_mode == "always":
                    try:
                        trace = scenectx.scenario_root / "trace.zip"
                        ui.stop_trace(trace)
                        scenectx.logger.info("ui_trace_saved", path=str(trace))
                    except Exception as e:
                        scenectx.logger.error("ui_trace_save_failed", error=str(e), traceback=traceback.format_exc())

                try:
                    ui.close()
                finally:
                    scenectx.logger.info("ui_session_closed")

            scenectx.logger.info("scenario_finished", status=scenario.status.name)
        

       

        trace = scenectx.get_service("trace")
        reqs = ",".join(trace.requirement_ids) if trace else ""

        trace_csv = behave_context.run_ctx.run_root / "traceability.csv"
        append_traceability_row(trace_csv, {
            "run_id": behave_context.run_ctx.run_id,
            "scenario_id": scenectx.scenario_id,
            "feature": scenario.feature.name,
            "scenario": scenario.name,
            "requirements": reqs,
        })

    def after_all(self, behave_context) -> None:
        if hasattr(behave_context, "run_ctx"):
            behave_context.run_ctx.logger.info("run_finished")

    # ----------------------------
    # Helpers
    # ----------------------------
    def _make_scenario_id(self, feature_name: str, scenario_name: str) -> str:
        raw = f"{feature_name}::{scenario_name}"
        h = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
        safe = "".join(c if c.isalnum() else "-" for c in scenario_name.lower()).strip("-")
        return f"{safe}-{h}"
