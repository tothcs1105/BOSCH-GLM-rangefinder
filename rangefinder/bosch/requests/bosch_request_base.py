from request import Request


class BoschRequestBase(Request):
    def __init__(self, command: int, extraPayload: [int]):
        self._command: int = command
        self._extraPayload: [int] = extraPayload
