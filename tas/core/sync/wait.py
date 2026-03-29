import time
from dataclasses import dataclass
from typing import Callable, Optional, Type, Tuple

from tas.core.errors.exceptions import TASTimeoutError

"""
    Generic polling-based wait utility for synchronizing test execution with system state.

    This class repeatedly evaluates a given condition until it becomes True or a timeout
    is reached. It is designed to handle asynchronous behavior in UI and API interactions,
    reducing test flakiness and improving execution stability.

    Features:
    - Configurable timeout and polling interval
    - Support for ignoring transient exceptions during evaluation
    - Optional timeout message customization
    - Integration with TAS error model via TASTimeoutError

    Typical Use Cases:
    - Waiting for UI elements to become visible or clickable
    - Polling API state until a desired condition is met
    - Synchronizing test steps with asynchronous system behavior

    Example:
        wait = Wait()
        wait.until(lambda: page.is_visible("login_button"))

    Design Note:
    This component is part of the Automation Core Layer (Synchronization & Retry)
    and is used across UI, API, and domain layers to ensure reliable test execution.
"""


@dataclass(frozen=True)
class WaitConfig:
    timeout_s: float = 10.0
    interval_s: float = 0.2

class Wait:
    def __init__(self, config: WaitConfig = WaitConfig()):
        self._cfg = config

    def until(
        self,
        condition: Callable[[], bool],
        timeout_s: Optional[float] = None,
        interval_s: Optional[float] = None,
        ignore_exceptions: Tuple[Type[BaseException], ...] = (),
        on_timeout: Optional[Callable[[], str]] = None,
    ) -> None:
        timeout = self._cfg.timeout_s if timeout_s is None else timeout_s
        interval = self._cfg.interval_s if interval_s is None else interval_s

        end = time.time() + timeout
        last_exc: Optional[BaseException] = None

        while time.time() < end:
            try:
                if condition():
                    return
            except ignore_exceptions as e:
                last_exc = e
            time.sleep(interval)

        msg = on_timeout() if on_timeout else "Wait condition timed out"
        if last_exc:
            msg += f" (last ignored: {type(last_exc).__name__}: {last_exc})"
        raise TASTimeoutError(msg)
