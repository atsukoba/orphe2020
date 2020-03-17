import binascii
import json
import time
from datetime import datetime

import bluepy.btle as btle
from bluepy.btle import Peripheral

H10_RAW = "AA:AA:AA:AA:AA:AA"


class MyDelegate(btle.DefaultDelegate):
    def __init__(self, params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        c_data = str(binascii.b2a_hex(data))
        # print(c_data)
        hr = int(c_data[2:4], 16)
        print(hr)

        data = {
            "createtime": '',
            "heart": 0
        }

        data['createtime'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
        data['heart'] = hr
        message = json.dumps(data)
        print(message)

class SensorMedal(Peripheral):
    def __init__(self, addr):
        Peripheral.__init__(self, addr, addrType="random")


def main():
    medal = SensorMedal(H10_RAW)
    medal.setDelegate(MyDelegate(btle.DefaultDelegate))
    medal.writeCharacteristic(0x0011, "\x01\x00", True)

    while True:
        if medal.waitForNotifications(1.0):
            continue


if __name__ == "__main__":
      
    print("ぴえん")
    # main()
