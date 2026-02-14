import os
import time
import uuid

# Who is executing test
def get_worker_id() -> str:
    # can later align with the  parallel runner choice
    return os.getenv("TAS_WORKER_ID") or os.getenv("PYTEST_XDIST_WORKER") or "w0"

# What execution session does test belong to
def new_run_id() -> str:
    
    ts = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    short = uuid.uuid4().hex[:8]
    return f"run-{ts}-{short}"