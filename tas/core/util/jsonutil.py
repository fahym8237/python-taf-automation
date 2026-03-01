import json
from typing import Any

def dumps_pretty(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True)

def loads(text: str) -> Any:
    return json.loads(text)
