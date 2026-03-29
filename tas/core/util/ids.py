import uuid
"""
Utility functions for generating unique identifiers used across the TAS framework.

This module provides lightweight helpers for creating correlation IDs and short
identifiers to support traceability, logging, and artifact naming.

Features:
- Generation of globally unique identifiers (UUID-based)
- Creation of compact identifiers for logs, filenames, and test runs

Typical Use Cases:
- Correlating logs across distributed components
- Assigning unique IDs to test runs or scenarios
- Naming artifacts such as reports, screenshots, or API captures

Functions:
- new_correlation_id(): Generates a full-length unique identifier
- short_id(): Generates a shortened unique identifier for concise usage

Design Note:
These utilities are part of the Automation Core Layer (Common Utilities)
and are widely used in observability and reporting components.
"""

def new_correlation_id() -> str:
    return uuid.uuid4().hex

def short_id(n: int = 8) -> str:
    return uuid.uuid4().hex[:n]
