from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

from tas.core.util.files import write_text
from tas.core.util.jsonutil import dumps_pretty

@dataclass(frozen=True)
class Attachment:
    name: str
    path: str
    mime: str

def write_attachments_index(scenario_root: Path, items: List[Attachment]) -> Optional[Path]:
    if not items:
        return None
    path = scenario_root / "attachments.json"
    payload = {"attachments": [asdict(x) for x in items]}
    return write_text(path, dumps_pretty(payload))