import smbus
import time

# Crea una instancia de smbus para la comunicación I2C
bus = smbus.SMBus(1)

# Direcciones I2C de los sensores
MPU6050_ADDRESS = 0x68
HMC5883L_ADDRESS = 0x1E

# Registros MPU6050
MPU6050_PWR_MGMT_1 = 0x6B
MPU6050_ACCEL_XOUT_H = 0x3B

# Registros HMC5883L
HMC5883L_MODE = 0x02
HMC5883L_XOUT_H = 0x03

# Inicializa el MPU6050
def inicializar_mpu6050():
    bus.write_byte_data(MPU6050_ADDRESS, MPU6050_PWR_MGMT_1, 0)

# Inicializa el HMC5883L
def inicializar_hmc5883l():
    bus.write_byte_data(HMC5883L_ADDRESS, HMC5883L_MODE, 0)

# Leer datos de 16 bits desde el sensor
def leer_datos_sensor(address, reg):
    high = bus.read_byte_data(address, reg)
    low = bus.read_byte_data(address, reg + 1)
    valor = (high << 8) + low
    if valor > 32767:
        valor -= 65536
    return valor

# Leer datos del acelerómetro
def leer_acelerometro():
    x = leer_datos_sensor(MPU6050_ADDRESS, MPU6050_ACCEL_XOUT_H)
    # Agrega aquí la lectura de los ejes Y y Z si es necesario
    return x

# Leer datos del magnetómetro
def leer_magnetometro():
    x = leer_datos_sensor(HMC5883L_ADDRESS, HMC5883L_XOUT_H)
    # Agrega aquí la lectura de los ejes Y y Z si es necesario
    return x

# Inicializar sensores
inicializar_mpu6050()
inicializar_hmc5883l()

# Bucle principal
try:
    while True:
        acel_data = leer_acelerometro()
        mag_data = leer_magnetometro()

        print(f"Datos del Acelerómetro: {acel_data}")
        print(f"Datos del Magnetómetro: {mag_data}")

        time.sleep(1)

except KeyboardInterrupt:
    print("Programa terminado por el usuario")
