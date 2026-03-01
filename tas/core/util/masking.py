from typing import Any, Dict

SENSITIVE_KEYS = {"password", "token", "authorization", "auth", "secret"}

def mask_dict(d: Dict[str, Any]) -> Dict[str, Any]:
    out = {}
    for k, v in d.items():
        if k and k.lower() in SENSITIVE_KEYS:
            out[k] = "***"
        else:
            out[k] = v
    return out
