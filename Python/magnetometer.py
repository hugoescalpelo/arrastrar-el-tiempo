import smbus
import time
import math

# Dirección del QMC5883L y registros
QMC5883L_ADDR = 0x0D
QMC5883L_DATA = 0x00
QMC5883L_CONFIG = 0x09
QMC5883L_RESET = 0x0B

# Valores de calibración
minX, maxX = -963, 1080
minY, maxY = 0, 2582

# Inicializar el bus I2C
bus = smbus.SMBus(1)  # 1 indica /dev/i2c-1

# Configuración del sensor
bus.write_byte_data(QMC5883L_ADDR, QMC5883L_RESET, 0x01)
bus.write_byte_data(QMC5883L_ADDR, QMC5883L_CONFIG, 0x1D)

def leerSensor():
    # Leer 6 bytes de datos: X LSB, X MSB, Y LSB, Y MSB, Z LSB, Z MSB
    data = bus.read_i2c_block_data(QMC5883L_ADDR, QMC5883L_DATA, 6)
    x = data[0] | data[1] << 8
    y = data[2] | data[3] << 8
    z = data[4] | data[5] << 8

    # Convertir a 16 bits
    if x > 32767:
        x -= 65536
    if y > 32767:
        y -= 65536
    if z > 32767:
        z -= 65536

    return x, y, z

def calcularAngulo(x, y):
    # Normalizar valores
    x = (x - minX) / (maxX - minX) * 65535 - 32768
    y = (y - minY) / (maxY - minY) * 65535 - 32768

    # Calcular el ángulo
    angulo = math.atan2(y, x)
    if angulo < 0:
        angulo += 2 * math.pi
    angulo = angulo * 180 / math.pi
    return angulo

def imprimirOrientacion(angulo):
    if angulo > 337.5 or angulo <= 22.5:
        return "N"
    elif angulo > 22.5 and angulo <= 67.5:
        return "NE"
    elif angulo > 67.5 and angulo <= 112.5:
        return "E"
    elif angulo > 112.5 and angulo <= 157.5:
        return "SE"
    elif angulo > 157.5 and angulo <= 202.5:
        return "S"
    elif angulo > 202.5 and angulo <= 247.5:
        return "SW"
    elif angulo > 247.5 and angulo <= 292.5:
        return "W"
    else:
        return "NW"

try:
    while True:
        x, y, z = leerSensor()
        angulo = calcularAngulo(x, y)
        orientacion = imprimirOrientacion(angulo)
        print(f"Ángulo: {angulo:.2f}°, Orientación: {orientacion}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa detenido.")
