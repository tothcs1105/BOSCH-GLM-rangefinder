from rangefinder import RangeFinder
from connection import Dispatcher
from request import Request
from .requests import BoschRequest192
from .requests.constants import AngleUnit, BacklightMode, MeasurementUnit


class BoschGlm(RangeFinder):
    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)

    def turnLaserOnOff(self, status: bool):
        if status:
            self._sendMessage(BoschRequest192(65))
        else:
            self._sendMessage(BoschRequest192(66))

    def changeSettings(
        self,
        setSpiritLevelEnabled: bool,
        setDispRotationEnabled: bool,
        setSpeakerEnabled: bool,
        setLaserPointerEnabled: bool,
        setBacklightMode: BacklightMode,
        setAngleUnit: AngleUnit,
        setMeasurementUnit: MeasurementUnit
            ):
        extraData = [
            int(setSpiritLevelEnabled),
            int(setDispRotationEnabled),
            int(setSpeakerEnabled),
            int(setLaserPointerEnabled),
            setBacklightMode.value,
            setAngleUnit.value,
            setMeasurementUnit.value]
        self._sendMessage(BoschRequest192(84, extraData))

    def _sendMessage(self, request: Request):
        self._dispatcher.send_Request(request.payload)
