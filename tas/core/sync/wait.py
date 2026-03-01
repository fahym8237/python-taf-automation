import time
from dataclasses import dataclass
from typing import Callable, Optional, Type, Tuple

from tas.core.errors.exceptions import TASTimeoutError

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
