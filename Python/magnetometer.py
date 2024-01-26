import smbus2
import time
import math

# Dirección I2C del HMC5883
HMC5883_ADDRESS = 0x1E

# Registros del HMC5883
HMC5883_REG_CONFIG_A = 0x00
HMC5883_REG_CONFIG_B = 0x01
HMC5883_REG_MODE = 0x02
HMC5883_REG_OUT_X_M = 0x03
HMC5883_REG_OUT_X_L = 0x04
HMC5883_REG_OUT_Z_M = 0x05
HMC5883_REG_OUT_Z_L = 0x06
HMC5883_REG_OUT_Y_M = 0x07
HMC5883_REG_OUT_Y_L = 0x08

# Configuración del sensor
def init_hmc5883():
    bus.write_byte_data(HMC5883_ADDRESS, HMC5883_REG_CONFIG_A, 0x70)
    bus.write_byte_data(HMC5883_ADDRESS, HMC5883_REG_CONFIG_B, 0xA0)
    bus.write_byte_data(HMC5883_ADDRESS, HMC5883_REG_MODE, 0x00)

# Leer datos del sensor
def read_hmc5883():
    data = bus.read_i2c_block_data(HMC5883_ADDRESS, HMC5883_REG_OUT_X_M, 6)
    x = (data[0] << 8) | data[1]
    z = (data[2] << 8) | data[3]
    y = (data[4] << 8) | data[5]

    if x > 32767:
        x -= 65536
    if y > 32767:
        y -= 65536
    if z > 32767:
        z -= 65536

    return x, y, z

# Calcular ángulo
def calculate_angle(x, y):
    angle = math.atan2(y, x)
    if angle < 0:
        angle += 2 * math.pi
    return math.degrees(angle)

# Determinar dirección
def direction(angle):
    dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
    return dirs[int(round((angle % 360) / 45))]

# Inicializar el bus I2C
bus = smbus2.SMBus(1)

# Inicializar el sensor
init_hmc5883()

# Bucle principal
while True:
    x, y, z = read_hmc5883()
    angle = calculate_angle(x, y)
    print("Ángulo: {:.2f}°, Dirección: {}".format(angle, direction(angle)))
    time.sleep(1)
