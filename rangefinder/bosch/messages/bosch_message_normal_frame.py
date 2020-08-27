from crccheck.crc import Crc
from .bosch_message import BoschMessage

class BoschMessageNormalFrame(BoschMessage):
    def __init__(self, command: int, extraPayload: [int] = []):
        super().__init__(command, extraPayload)

    @property
    def _frame(self) -> int:
        return 192

    @property
    def payload(self) -> bytearray:
        buffer = bytearray()
        buffer.append(self._frame)
        buffer.append(self._command)
        buffer.append(len(self._extraPayload))
        buffer.extend(bytearray(self._extraPayload))
        crcCalc = Crc(8, -0x5A, initvalue=-0x56)
        crcCalc.process(buffer)
        buffer.append(crcCalc.final())
        return buffer
    