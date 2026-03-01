import time

def iso_now_local() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

def epoch_ms() -> int:
    return int(time.time() * 1000)
