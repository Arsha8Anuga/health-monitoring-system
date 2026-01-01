from header import Header
from lib.envelope_pb2 import Envelope

class Packet : 
    def __init__ (self, header : Header , payload : Envelope) :
        self.header = header
        self.payload = payload