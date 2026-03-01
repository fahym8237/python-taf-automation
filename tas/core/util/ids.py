import uuid

def new_correlation_id() -> str:
    return uuid.uuid4().hex

def short_id(n: int = 8) -> str:
    return uuid.uuid4().hex[:n]
