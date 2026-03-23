import csv
from pathlib import Path
from typing import Dict, List

from tas.core.errors.exceptions import TASTestDataError

def load_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        raise TASTestDataError(f"Dataset not found: {path}")
    try:
        with path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except Exception as e:
        raise TASTestDataError(f"Failed to read CSV dataset {path}: {e}") from e

    if not rows:
        raise TASTestDataError(f"Dataset is empty: {path}")
    return rows