import time
from dataclasses import dataclass
from typing import Callable, Optional, Tuple, Type, TypeVar

"""
    Retry execution engine for handling transient failures in test operations.

    This class executes a given action with a retry strategy defined by
    RetryPolicy. It is designed to improve test stability by handling
    temporary issues such as network delays, asynchronous UI loading,
    or intermittent infrastructure failures.

    Features:
    - Configurable retry attempts and backoff strategy
    - Selective retry based on exception types
    - Optional callback hook for logging and observability

    Usage:
        retry = Retry(policy)
        result = retry.run(action)

    Example:
        retry.run(lambda: api.get_user())

    Design Note:
    This component belongs to the Automation Core Layer (Synchronization & Retry)
    and is widely used by UI interactions, API clients, and data provisioning logic.
"""

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
