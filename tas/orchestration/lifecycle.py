import hashlib
import os
from pathlib import Path

from tas.orchestration.parallel import get_worker_id, new_run_id
from tas.orchestration.artifacts import ArtifactManager
from tas.orchestration.logging import JsonlLogger, LogContext
from tas.orchestration.runner_context import RunContext, ScenarioContext
from tas.orchestration.tag_interpreter import TagInterpreter
from tas.interaction.ui.ui_session import UiSession, UiSessionConfig


class LifecycleManager:
    def __init__(self) -> None:
        self._tag_interpreter = TagInterpreter()

    def before_all(self, behave_context) -> None:
        worker_id = get_worker_id()
        run_id = new_run_id()

        artifact_root = Path("target") / "artifacts"
        am = ArtifactManager(artifact_root)
        run_root = am.ensure_run_root(run_id, worker_id)

        run_log = run_root / "run.log.jsonl"
        logger = JsonlLogger(run_log, LogContext(run_id=run_id, worker_id=worker_id))
        logger.info("run_started")

        behave_context.run_ctx = RunContext(
            run_id=run_id,
            worker_id=worker_id,
            run_root=run_root,
            logger=logger,
            services={"artifact_manager": am},
        )

    def before_scenario(self, behave_context, scenario) -> None:
        run_ctx: RunContext = behave_context.run_ctx
        am: ArtifactManager = run_ctx.services["artifact_manager"]

        scenario_id = self._make_scenario_id(scenario.feature.name, scenario.name)
        scenario_root = am.ensure_scenario_root(run_ctx.run_root, scenario_id)

        tags = self._tag_interpreter.interpret(scenario.feature, scenario)

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

        behave_context.scenario_ctx = ScenarioContext(
            scenario_id=scenario_id,
            scenario_root=scenario_root,
            tags=tags,
            logger=scenelog,
        )

        # --- UI session creation based on tags ---
        if tags.is_ui or tags.is_hybrid:
            browser = (tags.browser or os.getenv("TAS_BROWSER") or "chromium").strip()
            headless = (os.getenv("TAS_HEADLESS", "false").lower() == "true")
            trace_mode = os.getenv("TAS_TRACE", "off").strip()

            ui = UiSession(UiSessionConfig(
                browser=browser,
                headless=headless,
                trace_mode=trace_mode,
                artifacts_dir=scenario_root,
            ))
            ui.start()
            behave_context.scenario_ctx.set_service("ui", ui)
            scenelog.info("ui_session_started", browser=browser, headless=headless, trace_mode=trace_mode)


    def after_step(self, behave_context, step) -> None:
        if not hasattr(behave_context, "scenario_ctx"):
            return
        scenectx: ScenarioContext = behave_context.scenario_ctx
        scenectx.logger._ctx.step = step.name

        if step.status == "failed":
            scenectx.logger.error("step_failed", step=step.name)
       #on failure add screenshot + trace
        if step.status == "failed":
            ui = scenectx.get_service("ui")
            if ui:
                png = scenectx.scenario_root / "failure_screenshot.png"
                ui.screenshot(png)
                scenectx.logger.error("ui_screenshot_captured", path=str(png))

                trace_mode = os.getenv("TAS_TRACE", "off").strip()
                if trace_mode in ("on-failure", "always"):
                    trace = scenectx.scenario_root / "trace.zip"
                    ui.stop_trace(trace)
                    scenectx.logger.error("ui_trace_saved", path=str(trace))


    def after_scenario(self, behave_context, scenario) -> None:
        if not hasattr(behave_context, "scenario_ctx"):
            return
        scenectx: ScenarioContext = behave_context.scenario_ctx
        try:
            scenectx.cleanup()
        finally:
            scenectx.logger.info("scenario_finished", status=scenario.status.name)
        #close UI session and save trace if “always”
        ui = scenectx.get_service("ui")
        if ui:
            trace_mode = os.getenv("TAS_TRACE", "off").strip()
            if trace_mode == "always":
                trace = scenectx.scenario_root / "trace.zip"
                ui.stop_trace(trace)
                scenectx.logger.info("ui_trace_saved", path=str(trace))
            ui.close()
            scenectx.logger.info("ui_session_closed")


    def after_all(self, behave_context) -> None:
        if hasattr(behave_context, "run_ctx"):
            behave_context.run_ctx.logger.info("run_finished")

    def _make_scenario_id(self, feature_name: str, scenario_name: str) -> str:
        raw = f"{feature_name}::{scenario_name}"
        h = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
        # filesystem friendly
        safe = "".join(c if c.isalnum() else "-" for c in scenario_name.lower()).strip("-")
        return f"{safe}-{h}"