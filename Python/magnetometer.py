import smbus2
import time
import math

# Configura el bus I2C
bus = smbus2.SMBus(1)

# Dirección I2C del GY-87 (puede variar, verifica la documentación de tu sensor)
address = 0x68

# Configura el registro de control del magnetómetro
bus.write_byte_data(address, 0x37, 0x02)
bus.write_byte_data(address, 0x0A, 0x01)

def leer_brujula():
    # Lee los datos del magnetómetro
    data = bus.read_i2c_block_data(address, 0x03, 6)

    # Convierte los valores a un rango de 16 bits
    x = (data[0] << 8) | data[1]
    y = (data[4] << 8) | data[5]

    # Ajusta los valores negativos
    if x > 32767:
        x -= 65536
    if y > 32767:
        y -= 65536

    # Calcula el ángulo
    angulo = math.atan2(y, x)
    if angulo < 0:
        angulo += 2 * math.pi

    # Convierte a grados
    angulo = math.degrees(angulo)

    return angulo

def determinar_direccion(angulo):
    if angulo >= 45 and angulo < 135:
        return "Este"
    elif angulo >= 135 and angulo < 225:
        return "Sur"
    elif angulo >= 225 and angulo < 315:
        return "Oeste"
    else:
        return "Norte"

while True:
    angulo = leer_brujula()
    direccion = determinar_direccion(angulo)
    print(f"Ángulo: {angulo:.2f}°, Dirección: {direccion}")
    time.sleep(1)
