from lib.envelope_pb2 import Envelope
from lib.telemetry_pb2 import Telemetry
import time


telemetry = Telemetry()
telemetry.timestamp = int(time.time())
telemetry.cpu_name = "TestCPU"
telemetry.cpu_usage = 42.0
telemetry.ram_usage = "4GB / 16GB"

print("Telemetry object:")
print(telemetry)

envelope = Envelope()
envelope.telemetry.CopyFrom(telemetry)

print("Active payload:", envelope.WhichOneof("payload"))

data = envelope.SerializeToString()

print("Serialized bytes:", data)
print("Length:", len(data))

envelope2 = Envelope()
envelope2.ParseFromString(data)

print("Decoded envelope:")
print(envelope2)

print("Decoded payload type:", envelope2.WhichOneof("payload"))

decoded_telemetry = envelope2.telemetry
print(decoded_telemetry.cpu_name)
print(decoded_telemetry.cpu_usage)
