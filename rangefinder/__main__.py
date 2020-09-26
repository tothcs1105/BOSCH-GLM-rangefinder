import sys
import getopt
from connection import find, connect, Dispatcher
from bosch.bosch_glm import BoschGlm
from bosch.requests.constants import BacklightMode, AngleUnit, MeasurementUnit
from types import FunctionType

import unittest
from unittest.mock import call, Mock


def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]


def main(argv):
    # addr = connector.find('GLM50C')

    # socket = connector.connect(addr.addr, 0x0005)
    # print(socket)

    b = BoschGlm(Mock())
    b.changeSettings(False, False, False, False, BacklightMode.DISABLED, AngleUnit.DEGREE, MeasurementUnit.CM)

    for i in methods(BoschGlm):
        print(i)

    # if device.connected:
    #     print('Connected BOSCH '+ device.__class__.__name__ +'  @', device.bluetooth_address)

    #     try:
    #         print('\ntype \'m\' to measure, \n\'lon\' or \'loff\' to turn laser on/off, \n\'bon\' or \'boff\' to turn backlight on/off,\n\'x\' to exit\n')

    #         while True:
    #             data = input()
    #             if data == 'm':
    #                 distance = device.measure()
    #                 if distance > 0:
    #                     print(distance, 'mm from top of device')
    #                     print(distance+40.0, 'mm from tripod socket')
    #                     print(distance+110.0, 'mm from back of device')
    #             elif data == 'lon':
    #                 device.turn_laser_on()
    #             elif data == 'loff':
    #                 device.turn_laser_off()
    #             elif data == 'bon':
    #                 device.turn_backlight_on()
    #             elif data == 'boff':
    #                 device.turn_backlight_off()
    #             elif data == 'x':
    #                 device.close()
    #                 print('Connection to BOSCH ' + device.__class__.__name__ + ' closed')
    #                 break

    #     except KeyboardInterrupt:
    #         device.close()
    #         print('Connection to '+ device.__class__.__name__+' closed')
    # else:
    #     print('Could not connect to '+ device.__class__.__name__ )

if __name__ == "__main__":
    main(sys.argv[1:])