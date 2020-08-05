import bluetooth

def connect(bluetooth_address, port):
    try:
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        socket.connect((bluetooth_address, port))
        return socket
    except:
        socket.close()
        raise ConnectionError

def find(dev_bluetooth_name):
    print('Searching for ' + dev_bluetooth_name)
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    for item in enumerate(nearby_devices):
        addr, name = item[1]
        if dev_bluetooth_name in name:
            print('Found ' + name + ' @', addr)
            return item[1]