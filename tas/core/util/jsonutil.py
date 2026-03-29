import json
from typing import Any
"""
JSON utility helpers for serialization and deserialization operations.

This module centralizes JSON handling to ensure consistent formatting,
readability, and encoding across the TAF.

Features:
- Pretty-print JSON serialization with indentation and sorted keys
- Unicode-safe output for internationalization support
- Standardized JSON parsing

Typical Use Cases:
- Logging structured data in a readable format
- Storing API request/response payloads
- Exporting test artifacts and reports

Functions:
- dumps_pretty(): Serializes an object into a formatted JSON string
- loads(): Parses a JSON string into a Python object

Design Note:
Centralizing JSON utilities ensures consistency in logs and artifacts,
and simplifies integration with reporting and observability layers.
"""
def dumps_pretty(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True)

def loads(text: str) -> Any:
    return json.loads(text)
