from abc import ABCMeta, abstractmethod
from connection.dispatcher import Dispatcher
from message import Message

class RangeFinder(metaclass=ABCMeta):
    def __init__(self, dispatcher: Dispatcher):
        self._dispatcher = dispatcher

    @property
    def isConnected(self) -> bool:
        return self._dispatcher.isConnected()

    @abstractmethod
    def _sendMessage(self, Message):
        pass