from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional, Union


JsonType = Union[Dict[str, Any], list]


@dataclass(frozen=True)
class ApiResponse:
    url: str
    status: int
    headers: Dict[str, str]
    body_text: Optional[str]
    json: Optional[JsonType]
