from typing import Dict
from tas.core.util.ids import short_id

def with_unique_email(row: Dict[str, str], field: str = "email") -> Dict[str, str]:
    
    if field in row and row[field]:
        local, _, domain = row[field].partition("@")
        if domain:
            row = dict(row)
            row[field] = f"{local}+{short_id(6)}@{domain}"
    return row

def parse_bool(value: str) -> bool:
    return str(value).strip().lower() in ("true", "1", "yes", "y")