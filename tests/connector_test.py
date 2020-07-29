import unittest
from unittest.mock import call, Mock

import bluetooth
import rangefinder.connector as connector

class TestConnector(unittest.TestCase):

    def test_connect(self):
        address = 'test_address'
        port = 1010

        socket = Mock()
        bluetooth.BluetoothSocket = Mock(return_value = socket)

        result = connector.connect(address, port)

        self.assertEqual(result, socket)
        self.assertEqual(bluetooth.BluetoothSocket.mock_calls, [call(bluetooth.RFCOMM)])
        self.assertEqual(socket.mock_calls, [call.connect((address, port))])

    def test_find(self):
        dev_bluetooth_name = 'test_bl_name'
        nearby_devices = [('addr1','test1'), ('addr2','test2'), ('addr3','test_bl_name')]

        bluetooth.discover_devices = Mock(return_value = nearby_devices)

        result = connector.find(dev_bluetooth_name)

        self.assertEqual(result, ('addr3', dev_bluetooth_name))

if __name__ == '__main__':
    unittest.main()