import time
from dataclasses import dataclass
from typing import Callable, Optional, Tuple, Type, TypeVar

T = TypeVar("T")

@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 3
    backoff_s: float = 0.5
    retry_on: Tuple[Type[BaseException], ...] = ()

class Retry:
    def __init__(self, policy: RetryPolicy):
        self._p = policy

    def run(self, action: Callable[[], T], on_retry: Optional[Callable[[int, BaseException], None]] = None) -> T:
        attempt = 1
        while True:
            try:
                return action()
            except self._p.retry_on as e:
                if attempt >= self._p.max_attempts:
                    raise
                if on_retry:
                    on_retry(attempt, e)
                time.sleep(self._p.backoff_s * attempt)
                attempt += 1
