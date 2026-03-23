from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DatasetRef:
    name: str                 # e.g. "register_invalid.csv"
    path: Path                # resolved file path
    kind: str = "csv"         # csv/json/yaml (for later)