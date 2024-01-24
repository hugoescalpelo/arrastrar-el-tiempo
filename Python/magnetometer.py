import smbus2
import time
import math

class HMC5883L:
    def __init__(self):
        self.bus = smbus2.SMBus(1)
        self.address = 0x1E
        self.bus.write_byte_data(self.address, 0x00, 0x70)
        self.bus.write_byte_data(self.address, 0x01, 0xA0)
        self.bus.write_byte_data(self.address, 0x02, 0x00)

    def read_angle(self):
        data = self.bus.read_i2c_block_data(self.address, 0x03, 6)
        x = (data[0] << 8) | data[1]
        z = (data[2] << 8) | data[3]
        y = (data[4] << 8) | data[5]

        if x > 32767:
            x -= 65536
        if y > 32767:
            y -= 65536
        if z > 32767:
            z -= 65536

        angle = math.atan2(y, x)
        if angle < 0:
            angle += 2 * math.pi

        return math.degrees(angle)

    def cardinal_direction(self, angle):
        if angle > 315 or angle <= 45:
            return 'N'
        elif 45 < angle <= 135:
            return 'E'
        elif 135 < angle <= 225:
            return 'S'
        elif 225 < angle <= 315:
            return 'W'

sensor = HMC5883L()

try:
    while True:
        angle = sensor.read_angle()
        direction = sensor.cardinal_direction(angle)
        print(f"Dirección: {direction}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa terminado por el usuario")
