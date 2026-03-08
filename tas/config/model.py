from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class UiConfig:
    browser: str = "chromium"
    headless: bool = False
    trace_mode: str = "on-failure"   # off|on-failure|always

@dataclass(frozen=True)
class UiPilotUrls:
    login_url: str
    forgot_url: str
    register_url: str

@dataclass(frozen=True)
class ExecutionConfig:
    artifact_root: Path = Path("target") / "artifacts"

@dataclass(frozen=True)
class TasConfig:
    ui: UiConfig
    ui_pilot: UiPilotUrls
    exec: ExecutionConfig
