from abc import ABCMeta, abstractmethod

class Message(metaclass=ABCMeta):
    @property
    @abstractmethod
    def payload(self) -> bytearray:
        pass