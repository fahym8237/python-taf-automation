from dataclasses import dataclass
from typing import List, Set

@dataclass(frozen=True)
class TraceInfo:
    requirement_ids: List[str]   # e.g. ["REQ-AUTH-LOGIN-001"]

def extract_requirements(tags: Set[str]) -> TraceInfo:
    reqs = []
    for t in tags:
        # tags are raw like "trace=REQ-AUTH-LOGIN-001"
        if t.startswith("trace="):
            val = t.split("=", 1)[1].strip()
            if val:
                reqs.append(val)
    return TraceInfo(requirement_ids=sorted(set(reqs)))