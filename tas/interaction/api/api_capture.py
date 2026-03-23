from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class ApiLastExchange:
    method: str
    url: str
    request_headers: Dict[str, str]
    request_json: Optional[Dict[str, Any]]

    status: int
    response_headers: Dict[str, str]
    response_text: Optional[str]
    response_json: Optional[Any]
