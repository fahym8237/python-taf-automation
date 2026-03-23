

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

        # Set run context
        behave_context.run_ctx = RunContext(
            run_id=run_id,
            worker_id=worker_id,
            run_root=run_root,
            logger=logger,
            services={
                "artifact_manager": am,
                "config": cfg,
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

        scenectx = ScenarioContext(
            scenario_id=scenario_id,
            scenario_root=scenario_root,
            tags=tags,
            logger=scenelog,
        )
        behave_context.scenario_ctx = scenectx

        # Store a per-scenario data bag
        scenectx.set_service("data", {})

        # ----------------------------
        # Start UI session if needed
        # ----------------------------
        if tags.is_ui or tags.is_hybrid:
            browser = tags.browser or cfg.ui.browser
            headless = cfg.ui.headless
            trace_mode = cfg.ui.trace_mode

            try:
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
                scenelog.info(
                    "ui_session_started",
                    browser=browser,
                    headless=headless,
                    trace_mode=trace_mode,
                )
            except Exception as e:
                scenelog.error(
                    "ui_session_start_failed",
                    error=str(e),
                    traceback=traceback.format_exc(),
                )
                raise

        # ----------------------------
        # Start API session if needed (kept env-based until API config is added)
        # ----------------------------
        if tags.is_api or tags.is_hybrid:
            # For now we keep API base url env-based. Later Layer 7 expands config for API too.
            api_base_url = str(getattr(cfg, "api_base_url", "") or "").strip()
            if not api_base_url:
                # fallback to env if you haven't extended config model for API yet
                import os
                api_base_url = os.getenv("API_BASE_URL", "").strip()

            if not api_base_url:
                raise RuntimeError("Missing API base url (set -D api_base_url=... or env API_BASE_URL)")

            timeout_ms = int(getattr(cfg, "api_timeout_ms", 30000))

            try:
                api = ApiSession(
                    ApiSessionConfig(
                        base_url=api_base_url,
                        timeout_ms=timeout_ms,
                        default_headers=None,
                    )
                )
                api.start()
                scenectx.set_service("api", api)
                scenelog.info("api_session_started", base_url=api_base_url, timeout_ms=timeout_ms)
            except Exception as e:
                scenelog.error(
                    "api_session_start_failed",
                    error=str(e),
                    traceback=traceback.format_exc(),
                )
                raise

    def after_step(self, behave_context, step) -> None:
        if not hasattr(behave_context, "scenario_ctx"):
            return

        scenectx: ScenarioContext = behave_context.scenario_ctx
        scenectx.logger._ctx.step = step.name  # correlation context

        if step.status == "failed":
            scenectx.logger.error("step_failed", step=step.name)

            # UI failure diagnostics (screenshot + trace)
            ui: Optional[UiSession] = scenectx.get_service("ui")
            if ui:
                try:
                    png = scenectx.scenario_root / "failure_screenshot.png"
                    ui.screenshot(png)
                    scenectx.logger.error("ui_screenshot_captured", path=str(png))
                except Exception as e:
                    scenectx.logger.error("ui_screenshot_failed", error=str(e), traceback=traceback.format_exc())

                # trace mode comes from config via run_ctx
                trace_mode = behave_context.run_ctx.services["config"].ui.trace_mode
                if trace_mode in ("on-failure", "always"):
                    try:
                        trace = scenectx.scenario_root / "trace.zip"
                        ui.stop_trace(trace)
                        scenectx.logger.error("ui_trace_saved", path=str(trace))
                    except Exception as e:
                        scenectx.logger.error("ui_trace_save_failed", error=str(e), traceback=traceback.format_exc())

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
