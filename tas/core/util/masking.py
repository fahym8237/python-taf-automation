from typing import Any, Dict
"""
Sensitive data masking utilities for secure logging and reporting.

This module provides functions to sanitize dictionaries by masking
sensitive fields such as passwords, tokens, and authentication data
before they are logged or stored.

Features:
- Automatic masking of predefined sensitive keys
- Case-insensitive key matching
- Safe handling of structured data for observability

Typical Use Cases:
- Masking API request/response payloads in logs
- Preventing leakage of credentials in reports
- Ensuring compliance with security and privacy standards

Constants:
- SENSITIVE_KEYS: Set of keys considered sensitive (e.g., password, token)

Functions:
- mask_dict(): Returns a sanitized copy of a dictionary with sensitive values masked

Design Note:
This module is critical for maintaining security best practices within
the TAF, especially in CI/CD pipelines and shared logs.
"""

SENSITIVE_KEYS = {"password", "token", "authorization", "auth", "secret"}

def mask_dict(d: Dict[str, Any]) -> Dict[str, Any]:
    out = {}
    for k, v in d.items():
        if k and k.lower() in SENSITIVE_KEYS:
            out[k] = "***"
        else:
            out[k] = v
    return out
