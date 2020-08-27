from abc import ABCMeta, abstractmethod
from message import Message

class BoschMessage(Message):
    def __init__(self, command: int, extraPayload: [int]):
        self._command: int = command
        self._extraPayload: [int] = extraPayload

    @property
    @abstractmethod
    def _frame(self) -> int:
        pass