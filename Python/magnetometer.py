import smbus2
import time
import math

# Configura el bus I2C
bus = smbus2.SMBus(1)

# Dirección I2C del GY-87
address = 0x68

def inicializar_sensor():
    try:
        # Configura el registro de control del magnetómetro
        bus.write_byte_data(address, 0x37, 0x02)
        bus.write_byte_data(address, 0x0A, 0x01)
        print("Conexión con el sensor GY-87 establecida correctamente.")
        return True
    except Exception as e:
        print(f"Error al establecer conexión con el sensor: {e}")
        return False

def leer_brujula():
    try:
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
    except Exception as e:
        print(f"Error al leer los datos del sensor: {e}")
        return None

def determinar_direccion(angulo):
    if angulo >= 45 and angulo < 135:
        return "Este"
    elif angulo >= 135 and angulo < 225:
        return "Sur"
    elif angulo >= 225 and angulo < 315:
        return "Oeste"
    else:
        return "Norte"

if inicializar_sensor():
    while True:
        angulo = leer_brujula()
        if angulo is not None:
            direccion = determinar_direccion(angulo)
            print(f"Ángulo: {angulo:.2f}°, Dirección: {direccion}")
        else:
            print("No se pudo leer el ángulo.")
        time.sleep(1)
else:
    print("No se pudo inicializar el sensor.")
