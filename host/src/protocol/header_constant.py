from enum import Enum, IntFlag


MAGIC_BYTES = b'\x43\x90'
VERSION  = 1
PAYLOAD_LENGTH = 4

class MessageType(Enum) : 
    HANDSHAKE = 1
    PING = 2
    ACK = 3
    TELEMETRY = 4
    ERROR = 5

class HeaderFlags(IntFlag) : 
    NONE = 0
    URGENT = 1 << 0
    RESERVED = 1 << 1 