import smbus
import time

# Crea una instancia de smbus para la comunicación I2C
bus = smbus.SMBus(1)

# Direcciones I2C del acelerómetro y magnetómetro del GY-87
# Estas direcciones pueden variar, asegúrate de verificarlas
ACCEL_ADDRESS = 0xXX  
MAG_ADDRESS = 0xYY  

# Función para leer datos del acelerómetro
def leer_acelerometro():
    # Aquí necesitas escribir el código para leer los datos del acelerómetro
    # Esto incluye leer los registros adecuados a través de I2C
    # y convertir los valores leídos a unidades comprensibles (como m/s^2)
    pass

# Función para leer datos del magnetómetro
def leer_magnetometro():
    # Similar a leer_acelerometro, pero para el magnetómetro
    pass

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
