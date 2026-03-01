from enum import Enum

class FailureCategory(str, Enum):
    PRODUCT_DEFECT = "PRODUCT_DEFECT"
    TEST_DEFECT = "TEST_DEFECT"
    ENVIRONMENT = "ENVIRONMENT"
    INFRA = "INFRA"
    DATA = "DATA"
    CONFIG = "CONFIG"
    UNKNOWN = "UNKNOWN"
