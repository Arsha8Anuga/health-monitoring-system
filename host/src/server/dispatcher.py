from lib.envelope_pb2 import Envelope
from src.handlers import handshake, ping, ack, telemetry, error

class Dispatcher : 
    def dispatch(self, session, envelope : Envelope) : 
        payload_type = envelope.WhichOneOf("payload")

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
