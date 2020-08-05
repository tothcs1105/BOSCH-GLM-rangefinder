from connection.dispatcher import Dispatcher

class RangeFinder:
    
    def __init__(self, dispatcher: Dispatcher):
        self._dispatcher = dispatcher

    @property
    def isConnected(self) -> bool:
        return self._dispatcher.isConnected()

    