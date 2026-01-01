from enum import Enum

class Session : 
    def __init__ (self, conn) : 
        self.conn = conn
        self.state = SessionState.INIT
        self.client_id = None

class SessionState(Enum) : 
    INIT = 0, 
    READY = 1,
    AUTH = 2,
    CLOSED = 3