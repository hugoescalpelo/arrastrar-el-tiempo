import smbus
import time
import math

# Configura el bus I2C
bus = smbus.SMBus(1)

# Dirección del sensor QMC5883L
address = 0x0D

# Valores de calibración
minX, maxX = -1147, 1160
minY, maxY = 521, 2532

def read_raw_data(addr):
    # Lee dos bytes de datos desde addr
    low = bus.read_byte_data(address, addr)
    high = bus.read_byte_data(address, addr+1)

    # Combina ambos bytes
    value = ((high << 8) + low)

    # Ajusta a valor negativo si es necesario
    if (value > 32768):
        value = value - 65536
    return value

def get_heading(x, y):
    heading = math.atan2(y, x)
    # Ajuste por declinación magnética si es necesario
    # heading += declination

    # Convertir de radianes a grados
    heading = heading * 180/math.pi

    # Corrección de ángulo negativo
    if heading < 0:
        heading += 360

    return heading

def get_direction(heading):
    if heading >= 315 or heading < 45:
        return "N"
    elif 45 <= heading < 135:
        return "E"
    elif 135 <= heading < 225:
        return "S"
    elif 225 <= heading < 315:
        return "W"

try:
    while True:
        # Leer datos del sensor
        x = read_raw_data(0x01)
        y = read_raw_data(0x03)
        z = read_raw_data(0x05)

        # Calibración
        x_scaled = (x - minX) / (maxX - minX) * 2 - 1
        y_scaled = (y - minY) / (maxY - minY) * 2 - 1

        # Obtener ángulo y dirección
        heading = get_heading(x_scaled, y_scaled)
        direction = get_direction(heading)

        print("Ángulo:", heading, "Dirección:", direction)
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario")
