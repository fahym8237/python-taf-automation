from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from pathlib import Path

from tas.orchestration.logging import JsonlLogger, LogContext

@dataclass
class RunContext:
    run_id: str
    worker_id: str
    run_root: Path
    logger: JsonlLogger
    services: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ScenarioContext:
    scenario_id: str
    scenario_root: Path
    tags: Any
    logger: JsonlLogger
    state: Dict[str, Any] = field(default_factory=dict)
    cleanup_stack: list = field(default_factory=list)

    def add_cleanup(self, fn) -> None:
        self.cleanup_stack.append(fn)

    def cleanup(self) -> None:
        # Best-effort LIFO
        while self.cleanup_stack:
            fn = self.cleanup_stack.pop()
            try:
                fn()
            except Exception as e:
                self.logger.warn("cleanup_failed", error=str(e))