from __future__ import annotations

from pathlib import Path


def is_allure_available() -> bool:
    try:
        import allure  # noqa
        return True
    except Exception:
        return False


def attach_file_if_possible(name: str, path: Path) -> None:
    try:
        import allure
        from allure_commons.types import AttachmentType

        suffix = path.suffix.lower()

        if suffix == ".png":
            allure.attach.file(str(path), name=name, attachment_type=AttachmentType.PNG)
        elif suffix == ".json":
            allure.attach.file(str(path), name=name, attachment_type=AttachmentType.JSON)
        elif suffix == ".zip":
            allure.attach.file(str(path), name=name, attachment_type=AttachmentType.ZIP)
        elif suffix in (".txt", ".log", ".jsonl"):
            allure.attach.file(str(path), name=name, attachment_type=AttachmentType.TEXT)
        else:
            allure.attach.file(str(path), name=name)
    except Exception:
        return


def attach_text_if_possible(name: str, content: str) -> None:
    try:
        import allure
        from allure_commons.types import AttachmentType
        allure.attach(content, name=name, attachment_type=AttachmentType.TEXT)
    except Exception:
        return