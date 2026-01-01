from header import Header
from header_constant import HeaderFlags, FIELD_TYPE
from host.lib.envelope_pb2 import Envelope

def encode_message (envelope : Envelope , flags : HeaderFlags) :

    payload = envelope.SerializeToString()
    payload_name = envelope.WhichOneof("payload")

    if payload_name is None:
        raise ValueError("Envelope has no payload")
    
    msg_type = FIELD_TYPE[payload_name]

    header = Header(

        msg_type = msg_type,
        payload_len = len(payload),
        flags = flags

    )

    return header.encode() + payload