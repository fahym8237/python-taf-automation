"""
    This class serves as the root of the framework's error hierarchy,
    enabling consistent exception handling, classification, and reporting
    across all layers of the Test Automation framework.

    All custom framework exceptions should inherit from this class to allow:
    - Centralized error classification
    - Unified logging and observability
    - Integration with reporting and CI/CD pipelines
"""

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
