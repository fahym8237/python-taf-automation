import time

"""
Time utility helpers for standardized timestamp generation.

This module provides functions to retrieve the current time in commonly
used formats, supporting logging, reporting, and time-based operations
within the TAF.

Features:
- ISO-like local timestamp formatting
- Millisecond-precision epoch timestamps

Typical Use Cases:
- Timestamping logs and test events
- Generating unique time-based identifiers
- Measuring execution durations

Functions:
- iso_now_local(): Returns current local time in ISO-like format
- epoch_ms(): Returns current time in milliseconds since epoch

Design Note:
Standardizing time formats ensures consistency across logs, reports,
and distributed test execution environments.
"""

def iso_now_local() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

def epoch_ms() -> int:
    return int(time.time() * 1000)
