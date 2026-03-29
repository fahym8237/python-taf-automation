import json
import sys
from pathlib import Path


def scenario_status(scenario: dict) -> str:
    steps = scenario.get("steps", [])
    statuses = []
    for step in steps:
        result = step.get("result", {})
        status = str(result.get("status", "")).lower()
        if status:
            statuses.append(status)

    if not statuses:
        return "unknown"

    if any(s == "failed" for s in statuses):
        return "failed"
    if any(s == "passed" for s in statuses):
        return "passed"
    if all(s == "skipped" for s in statuses):
        return "skipped"
    return statuses[-1]


def filter_cucumber_json(input_path: Path, output_path: Path) -> None:
    data = json.loads(input_path.read_text(encoding="utf-8"))

    if not isinstance(data, list):
        raise RuntimeError("Expected top-level cucumber JSON to be a list")

    filtered_features = []

    for feature in data:
        elements = feature.get("elements", [])
        kept_elements = []

        for element in elements:
            status = scenario_status(element)

            # Keep only scenarios that were actually executed
            # passed / failed are kept
            # skipped / unknown are removed
            if status in ("passed", "failed"):
                kept_elements.append(element)

        if kept_elements:
            new_feature = dict(feature)
            new_feature["elements"] = kept_elements
            filtered_features.append(new_feature)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(filtered_features, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python scripts/filter_xray_cucumber_results.py <input_json> <output_json>")
        return 1

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    filter_cucumber_json(input_path, output_path)
    print(f"[XRAY] Filtered report written to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


