from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ArtifactPaths:
    run_root: Path
    scenario_root: Path

class ArtifactManager:
    def __init__(self, artifact_root: Path):
        self._artifact_root = artifact_root

    def ensure_run_root(self, run_id: str, worker_id: str) -> Path:
        run_root = self._artifact_root / f"{run_id}-{worker_id}"
        run_root.mkdir(parents=True, exist_ok=True)
        return run_root

    def ensure_scenario_root(self, run_root: Path, scenario_id: str) -> Path:
        scenario_root = run_root / scenario_id
        scenario_root.mkdir(parents=True, exist_ok=True)
        return scenario_root