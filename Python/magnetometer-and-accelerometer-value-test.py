import smbus
import time

# Crea una instancia de smbus para la comunicación I2C
bus = smbus.SMBus(1)

# Direcciones I2C para el GY-87
# Estas direcciones son ejemplos y pueden no ser las correctas para tu sensor
ACCEL_ADDRESS = 0x68
MAG_ADDRESS = 0x1E

# Registros específicos del acelerómetro y magnetómetro
# Deben ajustarse según las especificaciones del GY-87
ACCEL_XOUT_H = 0x3B
MAG_XOUT_H = 0x03

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
    x = leer_datos_sensor(ACCEL_ADDRESS, ACCEL_XOUT_H)
    # Agrega la lectura de los ejes Y y Z si es necesario
    return x

def leer_magnetometro():
    # Leer los valores del magnetómetro
    x = leer_datos_sensor(MAG_ADDRESS, MAG_XOUT_H)
    # Agrega la lectura de los ejes Y y Z si es necesario
    return x

# Bucle principal
try:
    while True:
        acel_x = leer_acelerometro()
        mag_x = leer_magnetometro()

        print(f"Valor del Acelerómetro (eje X): {acel_x}")
        print(f"Valor del Magnetómetro (eje X): {mag_x}")

        time.sleep(1)

except KeyboardInterrupt:
    print("Programa terminado por el usuario")
