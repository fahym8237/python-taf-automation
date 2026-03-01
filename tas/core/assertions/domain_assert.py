from dataclasses import dataclass
from typing import Any, Callable, Optional

from tas.core.errors.exceptions import TASAssertionError

@dataclass(frozen=True)
class _That:
    value: Any
    label: str = "value"

    def is_true(self, msg: Optional[str] = None) -> None:
        if not self.value:
            raise TASAssertionError(msg or f"Expected {self.label} to be True but was {self.value!r}")

    def is_false(self, msg: Optional[str] = None) -> None:
        if self.value:
            raise TASAssertionError(msg or f"Expected {self.label} to be False but was {self.value!r}")

    def is_equal_to(self, expected: Any, msg: Optional[str] = None) -> None:
        if self.value != expected:
            raise TASAssertionError(msg or f"Expected {self.label} == {expected!r} but was {self.value!r}")

    def is_not_none(self, msg: Optional[str] = None) -> None:
        if self.value is None:
            raise TASAssertionError(msg or f"Expected {self.label} to be not None")

    def is_positive_int(self, msg: Optional[str] = None) -> None:
        if not isinstance(self.value, int) or self.value <= 0:
            raise TASAssertionError(msg or f"Expected {self.label} to be positive int but was {self.value!r}")

    def matches(self, predicate: Callable[[Any], bool], msg: Optional[str] = None) -> None:
        ok = False
        try:
            ok = bool(predicate(self.value))
        except Exception as e:
            raise TASAssertionError(msg or f"Predicate raised {type(e).__name__}: {e}") from e
        if not ok:
            raise TASAssertionError(msg or f"Expected {self.label} to match predicate but was {self.value!r}")

class DomainAssert:
    @staticmethod
    def that(value: Any, label: str = "value") -> _That:
        return _That(value=value, label=label)

    @staticmethod
    def fail(msg: str) -> None:
        raise TASAssertionError(msg)
