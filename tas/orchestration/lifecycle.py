import hashlib
from pathlib import Path

from tas.orchestration.parallel import get_worker_id, new_run_id
from tas.orchestration.artifacts import ArtifactManager
from tas.orchestration.logging import JsonlLogger, LogContext
from tas.orchestration.runner_context import RunContext, ScenarioContext
from tas.orchestration.tag_interpreter import TagInterpreter

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

    def after_step(self, behave_context, step) -> None:
        if not hasattr(behave_context, "scenario_ctx"):
            return
        scenectx: ScenarioContext = behave_context.scenario_ctx
        scenectx.logger._ctx.step = step.name

        if step.status == "failed":
            scenectx.logger.error("step_failed", step=step.name)

    def after_scenario(self, behave_context, scenario) -> None:
        if not hasattr(behave_context, "scenario_ctx"):
            return
        scenectx: ScenarioContext = behave_context.scenario_ctx
        try:
            scenectx.cleanup()
        finally:
            scenectx.logger.info("scenario_finished", status=scenario.status.name)

    def after_all(self, behave_context) -> None:
        if hasattr(behave_context, "run_ctx"):
            behave_context.run_ctx.logger.info("run_finished")

    def _make_scenario_id(self, feature_name: str, scenario_name: str) -> str:
        raw = f"{feature_name}::{scenario_name}"
        h = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
        # filesystem friendly
        safe = "".join(c if c.isalnum() else "-" for c in scenario_name.lower()).strip("-")
        return f"{safe}-{h}"