from tas.core.errors.taxonomy import FailureCategory
from tas.core.errors import exceptions as ex

"""
    Classifies an exception into a standardized FailureCategory.

    This function maps framework-specific exceptions to high-level failure
    categories, enabling consistent reporting, analytics, and decision-making
    in CI/CD pipelines.

    Behavior:
    - Maps known TAF exceptions to predefined categories
    - Falls back to UNKNOWN for unrecognized exceptions
    - Supports future extensibility for more granular classification

    Example:
        TASAssertionError -> PRODUCT_DEFECT
        TASTestDataError -> DATA

    Usage:
        category = classify(exception)

    Design Note:
    This function is part of the Observability layer and is typically used
    after test execution to determine the root cause of failures.
"""

def classify(exc: BaseException) -> FailureCategory:
    if isinstance(exc, ex.TASAssertionError):
        return FailureCategory.PRODUCT_DEFECT
    if isinstance(exc, ex.TASTestDataError):
        return FailureCategory.DATA
    if isinstance(exc, ex.TASConfigurationError):
        return FailureCategory.CONFIG
    if isinstance(exc, ex.TASInfrastructureError):
        return FailureCategory.INFRA
    if isinstance(exc, ex.TASTimeoutError):
        # could be env or test; classify as UNKNOWN for now
        return FailureCategory.UNKNOWN
    return FailureCategory.UNKNOWN
