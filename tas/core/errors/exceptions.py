class TASBaseError(Exception):
    """Base framework exception."""

class TASAssertionError(AssertionError, TASBaseError):
    """Assertion failure. Usually indicates product defect."""

class TASTimeoutError(TASBaseError):
    """Wait timed out."""

class TASConfigurationError(TASBaseError):
    """Bad config or missing required configuration."""

class TASTestDataError(TASBaseError):
    """Dataset missing/invalid or data provisioning issue."""

class TASInfrastructureError(TASBaseError):
    """Browser/container/agent-level failure."""
