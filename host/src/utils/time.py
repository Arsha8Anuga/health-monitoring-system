import time 
from  datetime import datetime, timezone

def now_ts() -> float : 
    return time.time()

def now_dt() -> datetime : 
    return datetime.now(tz=timezone.utc)

def since(ts: float) -> float : 
    return now_ts() - ts

def ts_to_utc_str(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()