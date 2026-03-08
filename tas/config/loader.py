import os
from pathlib import Path

from tas.config.model import TasConfig, UiConfig, UiPilotUrls, ExecutionConfig
from tas.core.errors.exceptions import TASConfigurationError

def _get_ud(behave_context, key: str, default=None):
    # behave -D key=value becomes context.config.userdata["key"]
    return behave_context.config.userdata.get(key, default)

def load_config(behave_context) -> TasConfig:
    # UI pilot URLs (prefer -D, fallback to env)
    login_url = _get_ud(behave_context, "login_url") or os.getenv("LOGIN_URL")
    forgot_url = _get_ud(behave_context, "forgot_url") or os.getenv("FORGOT_URL")
    register_url = _get_ud(behave_context, "register_url") or os.getenv("REGISTER_URL")

    if not login_url or not forgot_url or not register_url:
        raise TASConfigurationError(
            "Missing UI pilot URLs. Provide via Behave user-data:\n"
            "  behave -D login_url=file:///.../login.html -D forgot_url=file:///.../forgot-password.html "
            "-D register_url=file:///.../register.html\n"
            "Or set env vars LOGIN_URL/FORGOT_URL/REGISTER_URL."
        )

    browser = _get_ud(behave_context, "browser") or os.getenv("TAS_BROWSER", "chromium")
    headless_raw = _get_ud(behave_context, "headless") or os.getenv("TAS_HEADLESS", "false")
    trace_mode = _get_ud(behave_context, "trace") or os.getenv("TAS_TRACE", "on-failure")

    headless = str(headless_raw).lower() == "true"

    artifact_root = _get_ud(behave_context, "artifact_root") or os.getenv("TAS_ARTIFACT_ROOT")
    artifact_root_path = Path(artifact_root) if artifact_root else (Path("target") / "artifacts")

    return TasConfig(
        ui=UiConfig(browser=str(browser), headless=headless, trace_mode=str(trace_mode)),
        ui_pilot=UiPilotUrls(login_url=login_url, forgot_url=forgot_url, register_url=register_url),
        exec=ExecutionConfig(artifact_root=artifact_root_path),
    )
