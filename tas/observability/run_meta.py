import platform
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any

from tas.core.util.timeutil import iso_now_local
from tas.core.util.files import write_text
from tas.core.util.jsonutil import dumps_pretty

@dataclass(frozen=True)
class RunMeta:
    run_id: str
    worker_id: str
    started_at: str
    python: str
    os: str

def write_run_meta(run_root: Path, run_id: str, worker_id: str) -> Path:
    meta = RunMeta(
        run_id=run_id,
        worker_id=worker_id,
        started_at=iso_now_local(),
        python=platform.python_version(),
        os=f"{platform.system()} {platform.release()}",
    )
    path = run_root / "run_meta.json"
    return write_text(path, dumps_pretty(asdict(meta)))

def write_environment_properties(allure_results_dir: Path, props: Dict[str, Any]) -> Path:
    # Allure reads environment.properties (key=value)
    lines = [f"{k}={v}" for k, v in props.items()]
    path = allure_results_dir / "environment.properties"
    return write_text(path, "\n".join(lines) + "\n")