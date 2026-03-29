import json
import os
import sys
from pathlib import Path

import requests

from tas.observability.exporters.xray_execution_info import build_default_execution_info


XRAY_AUTH_URL = "https://xray.cloud.getxray.app/api/v2/authenticate"
XRAY_IMPORT_CUCUMBER_MULTIPART_URL = "https://xray.cloud.getxray.app/api/v2/import/execution/cucumber/multipart"


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def parse_labels(raw: str) -> list[str]:
    if not raw:
        return []
    return [x.strip() for x in raw.split(",") if x.strip()]


def authenticate(client_id: str, client_secret: str) -> str:
    response = requests.post(
        XRAY_AUTH_URL,
        json={
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=30,
    )
    response.raise_for_status()

    token = response.text.strip().strip('"')
    if not token:
        raise RuntimeError("Xray authentication returned empty token")

    return token


def upload_multipart_results(token: str, cucumber_json_path: Path, execution_info: dict):
    if not cucumber_json_path.exists():
        raise FileNotFoundError(f"Missing file: {cucumber_json_path}")

    with cucumber_json_path.open("rb") as f:
        files = {
            "results": (cucumber_json_path.name, f, "application/json"),
            "info": ("info.json", json.dumps(execution_info).encode("utf-8"), "application/json"),
        }

        response = requests.post(
            XRAY_IMPORT_CUCUMBER_MULTIPART_URL,
            headers={"Authorization": f"Bearer {token}"},
            files=files,
            timeout=120,
        )

    return response


def main() -> int:
    try:
        client_id = require_env("XRAY_CLIENT_ID")
        client_secret = require_env("XRAY_CLIENT_SECRET")
        project_key = require_env("XRAY_PROJECT_KEY")

        report_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("target/xray/cucumber.json")

        run_kind = get_env("XRAY_RUN_KIND", "API Smoke")
        git_ref = get_env("GIT_REF", "local")
        build_id = get_env("BUILD_ID", "local-001")
        issue_type = get_env("XRAY_EXECUTION_ISSUE_TYPE", "Test Execution")

        # Increment 3 additions
        labels = parse_labels(get_env("XRAY_LABELS", "tas,api,smoke"))
        test_plan_key = get_env("XRAY_TEST_PLAN_KEY", "")
        environment = get_env("XRAY_ENVIRONMENT", "")

        execution_info = build_default_execution_info(
            project_key=project_key,
            run_kind=run_kind,
            issuetype_name=issue_type,
            git_ref=git_ref,
            build_id=build_id,
            labels=labels or None,
            test_plan_key=test_plan_key or None,
            environment=environment or None,
        ).to_dict()

        print("[XRAY] Authenticating...")
        token = authenticate(client_id, client_secret)

        print(f"[XRAY] Uploading multipart results from: {report_path}")
        print(f"[XRAY] Execution info: {json.dumps(execution_info, ensure_ascii=False)}")

        response = upload_multipart_results(token, report_path, execution_info)

        print(f"[XRAY] Status: {response.status_code}")
        print(response.text)

        response.raise_for_status()
        print("[XRAY] Multipart upload completed successfully.")
        return 0

    except Exception as e:
        print(f"[XRAY] Upload failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())