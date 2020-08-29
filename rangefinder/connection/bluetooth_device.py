class BluetoothDevice:
    def __init__(self, name: str, addr: str):
        self.__name = name
        self.__addr = addr

    @property
    def name(self) -> str:
        return self.__name

    @property
    def addr(self) -> str:
        return self.__addr
