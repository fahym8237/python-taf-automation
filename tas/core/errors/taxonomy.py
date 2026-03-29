from enum import Enum

"""
    Enumeration of standardized failure categories used for test result classification.

    This enum provides a controlled vocabulary to categorize failures across
    the TAF, enabling better reporting, analytics, and root cause analysis.

    Categories:
    - PRODUCT_DEFECT: Functional issue in the system under test
    - TEST_DEFECT: Issue in test logic or implementation
    - ENVIRONMENT: External system or environment instability
    - INFRA: Automation infrastructure failure
    - DATA: Test data-related issue
    - CONFIG: Configuration or setup problem
    - UNKNOWN: Unclassified or ambiguous failure

    Design Purpose:
    Used by the observability and reporting layers to aggregate and analyze
    test outcomes in CI/CD pipelines.
"""


class FailureCategory(str, Enum):
    PRODUCT_DEFECT = "PRODUCT_DEFECT"
    TEST_DEFECT = "TEST_DEFECT"
    ENVIRONMENT = "ENVIRONMENT"
    INFRA = "INFRA"
    DATA = "DATA"
    CONFIG = "CONFIG"
    UNKNOWN = "UNKNOWN"
