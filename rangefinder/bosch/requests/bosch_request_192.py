from crccheck.crc import Crc
from .bosch_request_base import BoschRequestBase

class BoschRequest192(BoschRequestBase):
    def __init__(self, command: int, extraPayload: [int] = []):
        super().__init__(command, extraPayload)

    @property
    def payload(self) -> bytearray:
        buffer = bytearray()
        buffer.append(192)
        buffer.append(self._command)
        buffer.append(len(self._extraPayload))
        buffer.extend(bytearray(self._extraPayload))
        crcCalc = Crc(8, -0x5A, initvalue=-0x56)
        crcCalc.process(buffer)
        buffer.append(crcCalc.final())
        return buffer