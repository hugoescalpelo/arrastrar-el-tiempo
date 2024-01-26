import smbus
import math
import time

# Configuración del bus I2C
bus = smbus.SMBus(1)  # 1 indica /dev/i2c-1
address = 0x0D

# Configuración del HMC5883L
def init_hmc5883l():
    bus.write_byte_data(address, 0x00, 0x70) # Configuración del registro A
    bus.write_byte_data(address, 0x01, 0xA0) # Configuración del registro B
    bus.write_byte_data(address, 0x02, 0x00) # Modo de medición continua

# Leer datos del HMC5883L
def read_hmc5883l():
    data = bus.read_i2c_block_data(address, 0x03, 6)
    x = (data[0] << 8) | data[1]
    z = (data[2] << 8) | data[3]
    y = (data[4] << 8) | data[5]
    
    if x >= 0x8000:
        x -= 0x10000
    if y >= 0x8000:
        y -= 0x10000
    if z >= 0x8000:
        z -= 0x10000

    return x, y, z

# Calcular ángulo
def calculate_heading(x, y):
    heading = math.atan2(y, x)
    if heading < 0:
        heading += 2 * math.pi
    return math.degrees(heading)

# Inicialización
init_hmc5883l()
time.sleep(1)

# Leer y mostrar el ángulo
while True:
    x, y, z = read_hmc5883l()
    heading = calculate_heading(x, y)
    print("Ángulo: {:.2f}°".format(heading))
    time.sleep(1)
