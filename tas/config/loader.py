import os
from pathlib import Path

from tas.config.model import TasConfig, UiConfig, UiPilotUrls, ExecutionConfig
from tas.core.errors.exceptions import TASConfigurationError
from tas.config.model import ApiConfig

def _get_ud(behave_context, key: str, default=None):
    # behave -D key=value becomes context.config.userdata["key"]
    return behave_context.config.userdata.get(key, default)

def load_config(behave_context) -> TasConfig:
    # UI pilot URLs (prefer -D, fallback to env)
    login_url = _get_ud(behave_context, "login_url") or os.getenv("LOGIN_URL")
    forgot_url = _get_ud(behave_context, "forgot_url") or os.getenv("FORGOT_URL")
    register_url = _get_ud(behave_context, "register_url") or os.getenv("REGISTER_URL")

    ui_pilot = UiPilotUrls(
        login_url=login_url,
        forgot_url=forgot_url,
        register_url=register_url,
    )

    if not login_url or not forgot_url or not register_url:
        ui_pilot = UiPilotUrls(
        login_url=login_url,
        forgot_url=forgot_url,
        register_url=register_url,
    )

    browser = _get_ud(behave_context, "browser") or os.getenv("TAS_BROWSER", "chromium")
    headless_raw = _get_ud(behave_context, "headless") or os.getenv("TAS_HEADLESS", "false")
    trace_mode = _get_ud(behave_context, "trace") or os.getenv("TAS_TRACE", "on-failure")

    headless = str(headless_raw).lower() == "true"

    artifact_root = _get_ud(behave_context, "artifact_root") or os.getenv("TAS_ARTIFACT_ROOT")
    artifact_root_path = Path(artifact_root) if artifact_root else (Path("target") / "artifacts")


    api_base_url = _get_ud(behave_context, "api_base_url") or os.getenv("API_BASE_URL")
    if not api_base_url:
        # allow UI-only runs; API runs will fail fast in before_scenario if missing
        api_base_url = ""

    api_timeout_ms_raw = _get_ud(behave_context, "api_timeout_ms") or os.getenv("API_TIMEOUT_MS", "30000")
    api_timeout_ms = int(api_timeout_ms_raw)

    api_ignore_raw = _get_ud(behave_context, "api_ignore_https_errors") or os.getenv("API_IGNORE_HTTPS_ERRORS", "false")
    api_ignore = _to_bool(api_ignore_raw)

    api=ApiConfig(
        base_url=api_base_url or "",
        timeout_ms=api_timeout_ms,
        default_headers=None,
        ignore_https_errors=api_ignore,  # ✅ critical
    ),



    return TasConfig(
        ui=UiConfig(browser=str(browser), headless=headless, trace_mode=str(trace_mode)),
        ui_pilot=UiPilotUrls(login_url=login_url, forgot_url=forgot_url, register_url=register_url),
        api=ApiConfig(base_url=api_base_url, timeout_ms=api_timeout_ms, default_headers=None, ignore_https_errors=api_ignore),
        exec=ExecutionConfig(artifact_root=artifact_root_path),
    )

def _to_bool(v) -> bool:
    return str(v).strip().lower() in ("true", "1", "yes", "y")
