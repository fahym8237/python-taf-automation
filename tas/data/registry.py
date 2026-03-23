from pathlib import Path
from typing import List, Dict

from tas.core.errors.exceptions import TASTestDataError
from tas.data.dataset_ref import DatasetRef
from tas.data.loaders.csv_loader import load_csv

DATA_ROOT = Path("features") / "data"

def resolve_dataset(name: str) -> DatasetRef:
    path = DATA_ROOT / name
    kind = "csv" if name.lower().endswith(".csv") else "unknown"
    return DatasetRef(name=name, path=path, kind=kind)

def load_dataset(ref: DatasetRef) -> List[Dict[str, str]]:
    if ref.kind == "csv":
        return load_csv(ref.path)
    raise TASTestDataError(f"Unsupported dataset type for {ref.name} (kind={ref.kind})")