from enum import Enum
from src.utils.time import now_ts

class Session : 
    def __init__ (self, conn) : 
        self.conn = conn
        self.state = SessionState.INIT
        self.client_id = None
        self.last_seen = now_ts()
        self.flags = set()

class SessionState(Enum) : 
    INIT = 0, 
    READY = 1,
    AUTH = 2,
    CLOSED = 3