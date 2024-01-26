import smbus
import time
import math

# Configuración del bus I2C
bus = smbus.SMBus(1)  # Utiliza 0 para Raspberry Pi Model A y Model B de la primera generación
address = 0x0D

def read_sensor():
    # Leer los datos del sensor
    data = bus.read_i2c_block_data(address, 0x00, 6)

    # Convertir los datos
    x = data[0] * 256 + data[1]
    if x > 32767:
        x -= 65536
    y = data[2] * 256 + data[3]
    if y > 32767:
        y -= 65536
    z = data[4] * 256 + data[5]
    if z > 32767:
        z -= 65536

    return x, y, z

def calculate_heading(x, y):
    angle = math.atan2(y, x)
    if angle < 0:
        angle += 2 * math.pi
    return math.degrees(angle)

def get_orientation(heading):
    if heading >= 315 or heading < 45:
        return 'N'
    elif 45 <= heading < 135:
        return 'E'
    elif 135 <= heading < 225:
        return 'S'
    elif 225 <= heading < 315:
        return 'W'

try:
    while True:
        x, y, z = read_sensor()
        heading = calculate_heading(x, y)
        orientation = get_orientation(heading)
        print("Ángulo: {:.2f}°, Orientación: {}".format(heading, orientation))
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa terminado por el usuario")
