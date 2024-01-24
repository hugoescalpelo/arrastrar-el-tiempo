import smbus
import time

# Crea una instancia de smbus para la comunicación I2C
bus = smbus.SMBus(1)

# Direcciones I2C para el GY-87 actualizadas
ACCEL_ADDRESS = 0x77
MAG_ADDRESS = 0x68

# Registros específicos del acelerómetro y magnetómetro
# Ajusta estos según el datasheet del GY-87
ACCEL_REG = 0xXX  # Reemplaza XX con el registro correcto
MAG_REG = 0xXX    # Reemplaza XX con el registro correcto

def leer_datos_sensor(address, reg):
    # Leer datos de 16 bits (dos registros)
    high = bus.read_byte_data(address, reg)
    low = bus.read_byte_data(address, reg + 1)

    # Convertir los valores
    valor = (high << 8) + low

    # Corregir signo del valor
    if valor > 32767:
        valor -= 65536
    return valor

def leer_acelerometro():
    # Leer los valores del acelerómetro
    x = leer_datos_sensor(ACCEL_ADDRESS, ACCEL_REG)
    # Agrega la lectura de los ejes Y y Z si es necesario
    return x

def leer_magnetometro():
    # Leer los valores del magnetómetro
    x = leer_datos_sensor(MAG_ADDRESS, MAG_REG)
    # Agrega la lectura de los ejes Y y Z si es necesario
    return x

# Bucle principal
try:
    while True:
        acel_data = leer_acelerometro()
        mag_data = leer_magnetometro()

        print("Datos del Acelerómetro:", acel_data)
        print("Datos del Magnetómetro:", mag_data)

        time.sleep(1)

except KeyboardInterrupt:
    print("Programa terminado por el usuario")
