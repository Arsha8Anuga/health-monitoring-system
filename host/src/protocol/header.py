from header_constant import MAGIC_BYTES, VERSION, MessageType, HeaderFlags, PAYLOAD_LENGTH

class Header: 
    def __init__(self, magic : bytes = MAGIC_BYTES, 
                 version : int = VERSION,
                 msg_type : MessageType = MessageType.HANDSHAKE,
                 flags :  HeaderFlags = HeaderFlags.NONE,
                 payload_len : int = PAYLOAD_LENGTH
                 ) : 
        
        self.magic = magic 
        self.version = version
        self.msg_type = msg_type
        self.flags = flags
        self.payload_len = payload_len
    

    def encode(self) -> bytes:
        return (
            self.magic +
            self.version.to_bytes(1, 'big') +
            self.msg_type.value.to_bytes(1, 'big') +
            self.flags.value.to_bytes(1, 'big') +
            self.payload_len.to_bytes(4, 'big')
        )

    @classmethod
    def decode(cls, data : bytes) :

        if len(data) < 9 :
            raise ValueError("ERROR : Header isn't complete.")

        magic = data[0:2]
        version = data[2]
        msg_type =  MessageType(data[3])
        flags = HeaderFlags(data[4])
        payload_len = int.from_bytes(data[5:9], 'big')
        
        return cls(
            magic = magic, 
            version = version, 
            msg_type = msg_type, 
            flags = flags, 
            payload_len = payload_len
        )
    
    def validate(self) -> bool :
        return self.magic == MAGIC_BYTES and self.version >= VERSION 

