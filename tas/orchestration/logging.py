import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

#defines the execution identity envelope
@dataclass
class LogContext:
    run_id: str
    worker_id: str
    scenario_id: Optional[str] = None
    feature: Optional[str] = None
    scenario: Optional[str] = None
    step: Optional[str] = None

class JsonlLogger:
    def __init__(self, file_path: Path, ctx: LogContext):
        self._file_path = file_path
        self._ctx = ctx

    def info(self, event: str, **fields: Any) -> None:
        self._write("INFO", event, fields)

    def warn(self, event: str, **fields: Any) -> None:
        self._write("WARN", event, fields)

    def error(self, event: str, **fields: Any) -> None:
        self._write("ERROR", event, fields)

    def _write(self, level: str, event: str, fields: Dict[str, Any]) -> None:
        record = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
            "level": level,
            "event": event,
            "run_id": self._ctx.run_id,
            "worker_id": self._ctx.worker_id,
            "scenario_id": self._ctx.scenario_id,
            "feature": self._ctx.feature,
            "scenario": self._ctx.scenario,
            "step": self._ctx.step,
            **fields,
        }
        line = json.dumps(record, ensure_ascii=False)
        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        with self._file_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")