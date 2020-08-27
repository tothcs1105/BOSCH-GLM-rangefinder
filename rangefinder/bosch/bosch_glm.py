from rangefinder import RangeFinder
from connection import Dispatcher
from message import Message
from messages import BoschMessageNormalFrame
from constants import BacklightMode

class BoschGlm(RangeFinder):
    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)

    def turnLaserOnOff(self, status: bool):
        if status:
            self._sendMessage(BoschMessageNormalFrame(65))
        else:
            self._sendMessage(BoschMessageNormalFrame(66))

    def _sendMessage(self, message: Message):
        self._dispatcher.send_Request(message.payload)