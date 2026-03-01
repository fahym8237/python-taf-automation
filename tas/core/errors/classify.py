from tas.core.errors.taxonomy import FailureCategory
from tas.core.errors import exceptions as ex

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
