import smbus
import time
import math

# Dirección I2C del QMC5883L
QMC5883L_ADDR = 0x0D

# Registros del QMC5883L
QMC5883L_X_LSB = 0x00
QMC5883L_CONFIG = 0x09

def init_qmc5883l():
    bus.write_byte_data(QMC5883L_ADDR, QMC5883L_CONFIG, 0x01)

def read_qmc5883l():
    data = bus.read_i2c_block_data(QMC5883L_ADDR, QMC5883L_X_LSB, 6)
    x = data[0] | data[1] << 8
    y = data[2] | data[3] << 8
    z = data[4] | data[5] << 8

    # Convertir a 16 bits si es necesario
    if x > 32767:
        x -= 65536
    if y > 32767:
        y -= 65536
    if z > 32767:
        z -= 65536

    return x, y, z

def calculate_heading(x, y):
    heading = math.atan2(y, x)
    if heading < 0:
        heading += 2 * math.pi
    heading = math.degrees(heading)
    return heading

def get_orientation(heading):
    if heading < 45 or heading >= 315:
        return 'N'
    elif heading < 135:
        return 'E'
    elif heading < 225:
        return 'S'
    else:
        return 'W'

# Inicializar I2C (smbus)
bus = smbus.SMBus(1)  # Usar 0 para modelos antiguos de Raspberry Pi

# Inicializar el sensor QMC5883L
init_qmc5883l()

try:
    while True:
        x, y, z = read_qmc5883l()
        heading = calculate_heading(x, y)
        orientation = get_orientation(heading)
        print(f"Ángulo: {heading:.2f} grados, Orientación: {orientation}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa terminado por el usuario")
