from tas.core import DomainAssert, Wait, WaitConfig
from tas.core.sync.retry import Retry, RetryPolicy
from tas.core.errors.exceptions import TASAssertionError, TASTimeoutError

def test_assert():
    DomainAssert.that(True, "flag").is_true()
    try:
        DomainAssert.that(False, "flag").is_true()
        raise RuntimeError("should have failed")
    except TASAssertionError:
        pass

def test_wait():
    w = Wait(WaitConfig(timeout_s=0.5, interval_s=0.1))
    try:
        w.until(lambda: False)
        raise RuntimeError("should have timed out")
    except TASTimeoutError:
        pass

def test_retry():
    attempts = {"n": 0}
    def action():
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise ValueError("transient")
        return "ok"
    r = Retry(RetryPolicy(max_attempts=3, backoff_s=0.01, retry_on=(ValueError,)))
    assert r.run(action) == "ok"

if __name__ == "__main__":
    test_assert()
    test_wait()
    test_retry()
    print("Layer 5 core smoke OK")
