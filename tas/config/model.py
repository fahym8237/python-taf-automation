from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict

@dataclass(frozen=True)
class UiConfig:
    browser: str = "chromium"
    headless: bool = False
    trace_mode: str = "on-failure"   # off|on-failure|always

@dataclass(frozen=True)
class UiPilotUrls:
    login_url: Optional[str] = None
    forgot_url: Optional[str] = None
    register_url: Optional[str] = None

@dataclass(frozen=True)
class ExecutionConfig:
    artifact_root: Path = Path("target") / "artifacts"

@dataclass(frozen=True)
class ApiConfig:
    base_url: str
    timeout_ms: int = 30_000
    default_headers: Optional[Dict[str, str]] = None
    ignore_https_errors: bool = False

@dataclass(frozen=True)
class TasConfig:
    ui: UiConfig
    ui_pilot: UiPilotUrls
    api: ApiConfig
    exec: ExecutionConfig

