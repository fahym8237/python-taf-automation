import json
import os
from pathlib import Path
from threading import Lock


class RuntimeCredentials:
    _lock = Lock()

    _file_path = Path(
        os.getenv(
            "RUNTIME_CREDENTIALS_FILE",
            "target/runtime/runtime_credentials.json"
        )
    )

    @classmethod
    def _ensure_file_exists(cls) -> None:
        cls._file_path.parent.mkdir(parents=True, exist_ok=True)

        if cls._file_path.exists():
            return

        login_email = os.getenv("LOGIN_EMAIL")
        login_password = os.getenv("LOGIN_PASSWORD")

        if not login_email:
            raise RuntimeError("LOGIN_EMAIL is not configured")

        if not login_password:
            raise RuntimeError("LOGIN_PASSWORD is not configured")

        cls._write({
            "LOGIN_EMAIL": login_email,
            "LOGIN_PASSWORD": login_password,
        })

    @classmethod
    def _read(cls) -> dict:
        cls._ensure_file_exists()
        with cls._file_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def _write(cls, data: dict) -> None:
        cls._file_path.parent.mkdir(parents=True, exist_ok=True)
        with cls._file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def get_login_email(cls) -> str:
        with cls._lock:
            return cls._read()["LOGIN_EMAIL"]

    @classmethod
    def get_login_password(cls) -> str:
        with cls._lock:
            return cls._read()["LOGIN_PASSWORD"]

    @classmethod
    def set_login_email(cls, email: str) -> None:
        if not email:
            raise RuntimeError("Cannot set empty LOGIN_EMAIL")

        with cls._lock:
            data = cls._read()
            data["LOGIN_EMAIL"] = email
            cls._write(data)

    @classmethod
    def set_login_password(cls, password: str) -> None:
        if not password:
            raise RuntimeError("Cannot set empty LOGIN_PASSWORD")

        with cls._lock:
            data = cls._read()
            data["LOGIN_PASSWORD"] = password
            cls._write(data)

    @classmethod
    def reset(cls) -> None:
        with cls._lock:
            if cls._file_path.exists():
                cls._file_path.unlink()