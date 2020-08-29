from abc import ABCMeta, abstractmethod


class Request(metaclass=ABCMeta):
    @property
    @abstractmethod
    def payload(self) -> bytearray:
        pass
