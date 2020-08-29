import bluetooth


class Dispatcher:
    def __init__(self, socket: bluetooth.BluetoothSocket):
        self.__socket = socket

    @property
    def is_connected(self) -> bool:
        return self.__socket.connected

    def send_Request(self, request):
        self.__socket.send(request)
