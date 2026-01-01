from header import Header
from host.lib.envelope_pb2 import Envelope
from google.protobuf.message import DecodeError

class StreamParser :
    def __init__(self) : 
        self.buffer = bytearray()

    def feed(self, data : bytes) :

        self.buffer.extend(data)
        messages = []

        while True : 

            if len(self.buffer) < 9 :
                break 

            header_bytes = self.buffer[:9]
            header = Header.decode(header_bytes)

            if not Header.validate(header) : 
                raise ValueError("Invalid Header")
            
            total_len = 9 + header.payload_len
            if len(self.buffer) < total_len : 
                break

            payload = bytes(self.buffer[9:total_len])
            del self.buffer[:total_len]

            try :
                env = Envelope()
                env.ParseFromString(payload)

            except  DecodeError as e:
                raise ValueError("Invalid Payload") from e
                
            messages.append(env)
        
        return messages
    
