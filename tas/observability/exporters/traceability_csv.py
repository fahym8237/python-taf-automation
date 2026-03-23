import csv
from pathlib import Path
from typing import List, Dict

def append_traceability_row(trace_csv: Path, row: Dict[str, str]) -> None:
    trace_csv.parent.mkdir(parents=True, exist_ok=True)
    exists = trace_csv.exists()
    with trace_csv.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["run_id", "scenario_id", "feature", "scenario", "requirements"])
        if not exists:
            writer.writeheader()
        writer.writerow(row)