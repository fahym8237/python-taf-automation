import os
import sys
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

import requests


XRAY_AUTH_URL = "https://xray.cloud.getxray.app/api/v2/authenticate"
XRAY_IMPORT_FEATURES_URL = "https://xray.cloud.getxray.app/api/v2/import/feature"


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def authenticate(client_id: str, client_secret: str) -> str:
    response = requests.post(
        XRAY_AUTH_URL,
        json={"client_id": client_id, "client_secret": client_secret},
        timeout=30,
    )
    response.raise_for_status()
    token = response.text.strip().strip('"')
    if not token:
        raise RuntimeError("Xray authentication returned an empty token")
    return token


def build_features_zip(root: Path, zip_path: Path) -> int:
    feature_files = sorted(root.rglob("*.feature"))
    if not feature_files:
        raise RuntimeError(f"No .feature files found under: {root}")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for feature_file in feature_files:
            # preserve relative path inside zip
            arcname = feature_file.relative_to(root.parent)
            zf.write(feature_file, arcname=str(arcname))

    return len(feature_files)


def import_features_zip(token: str, zip_path: Path, project_key: str) -> requests.Response:
    with zip_path.open("rb") as f:
        response = requests.post(
            f"{XRAY_IMPORT_FEATURES_URL}?projectKey={project_key}",
            headers={
                "Authorization": f"Bearer {token}",
            },
            files={
                "file": (zip_path.name, f, "application/zip"),
            },
            timeout=120,
        )
    return response


def main() -> int:
    try:
        client_id = require_env("XRAY_CLIENT_ID")
        client_secret = require_env("XRAY_CLIENT_SECRET")
        project_key = require_env("XRAY_PROJECT_KEY")

        root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("features/api")
        if not root.exists():
            raise RuntimeError(f"Path does not exist: {root}")

        print("[XRAY] Authenticating...")
        token = authenticate(client_id, client_secret)

        with TemporaryDirectory() as tmpdir:
            zip_path = Path(tmpdir) / "features.zip"
            count = build_features_zip(root, zip_path)
            print(f"[XRAY] Built zip with {count} feature file(s): {zip_path}")

            print(f"[XRAY] Importing zipped features into project {project_key}...")
            response = import_features_zip(token, zip_path, project_key)

            print(f"[XRAY] Status: {response.status_code}")
            print(response.text)

            response.raise_for_status()
            print("[XRAY] Feature import completed successfully.")
            return 0

    except Exception as e:
        print(f"[XRAY] Feature import failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())