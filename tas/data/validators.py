from typing import Dict, List
from tas.core.errors.exceptions import TASTestDataError

def require_columns(rows: List[Dict[str, str]], required: List[str], dataset_name: str) -> None:
    missing = [c for c in required if c not in rows[0]]
    if missing:
        raise TASTestDataError(f"Dataset '{dataset_name}' missing columns: {missing}")