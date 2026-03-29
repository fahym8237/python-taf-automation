import json
import os
import sys
from pathlib import Path

import requests


XRAY_AUTH_URL = "https://xray.cloud.getxray.app/api/v2/authenticate"
XRAY_IMPORT_CUCUMBER_URL = "https://xray.cloud.getxray.app/api/v2/import/execution/cucumber"


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


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
        raise RuntimeError("Xray authentication succeeded but returned an empty token")
    return token


def upload_cucumber_results(token: str, cucumber_json_path: Path) -> requests.Response:
    if not cucumber_json_path.exists():
        raise FileNotFoundError(f"Cucumber JSON file not found: {cucumber_json_path}")

    with cucumber_json_path.open("rb") as f:
        response = requests.post(
            XRAY_IMPORT_CUCUMBER_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            data=f.read(),
            timeout=60,
        )

    return response


def main() -> int:
    try:
        client_id = require_env("XRAY_CLIENT_ID")
        client_secret = require_env("XRAY_CLIENT_SECRET")
        report_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("target/xray/cucumber.json")

        print(f"[XRAY] Authenticating...")
        token = authenticate(client_id, client_secret)

        print(f"[XRAY] Uploading results from: {report_path}")
        response = upload_cucumber_results(token, report_path)

        print(f"[XRAY] Status: {response.status_code}")
        print(response.text)

        response.raise_for_status()
        print("[XRAY] Upload completed successfully.")
        return 0

    except Exception as e:
        print(f"[XRAY] Upload failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())