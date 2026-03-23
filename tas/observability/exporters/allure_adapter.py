from pathlib import Path
from typing import Optional

def is_allure_available() -> bool:
    try:
        import allure  # noqa
        return True
    except Exception:
        return False

def attach_file_if_possible(name: str, path: Path, mime: str) -> None:
    try:
        import allure
        allure.attach.file(str(path), name=name, attachment_type=mime)
    except Exception:
        # No hard dependency
        return