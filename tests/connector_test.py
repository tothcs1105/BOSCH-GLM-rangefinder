import unittest
import rangefinder.connector as connector

class TestConnector(unittest.TestCase):

    def test_connect(self):
         self.assertFalse(connector.connect('',''))

if __name__ == '__main__':
    unittest.main()