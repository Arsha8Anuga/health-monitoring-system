from src.handlers import handshake, ping, ack, telemetry, error
from src.protocol.header_constant import FIELD_TYPE, HeaderFlags
from src.protocol.packet import Packet

class Dispatcher : 
    def dispatch(self, session, pkt: Packet) :

        envelope = pkt.payload
        header = pkt.header

        payload_type = envelope.WhichOneOf("payload")

        if FIELD_TYPE[payload_type] !=  header.msg_type : 
            raise ValueError("Protocol Violation : header and payload type mismatch.")
        
        if header.flags & HeaderFlags.URGENT : 
            pass

        if payload_type == "handshake":
            handshake.handle(session, envelope.handshake)

        elif payload_type == "telemetry":
            telemetry.handle(session, envelope.telemetry)

        elif payload_type == "ping":
            ping.handle(session, envelope.ping)
        
        elif payload_type == "ack" : 
            ack.handle(session, envelope.ack)

        elif payload_type == "error":
            error.handle(session, envelope.error)

        else:
            raise ValueError("Unknown payload type")
