import smbus
import time
import math

# Dirección I2C del QMC5883L
QMC5883L_ADDR = 0x0D

# Crear una instancia de smbus para la comunicación I2C
bus = smbus.SMBus(1)  # 1 indica /dev/i2c-1

# Función para inicializar el sensor
def init_sensor():
    bus.write_byte_data(QMC5883L_ADDR, 0x0B, 0x01)
    bus.write_byte_data(QMC5883L_ADDR, 0x09, 0x1D)

# Función para leer datos del sensor
def leer_sensor():
    bus.write_byte(QMC5883L_ADDR, 0x00)
    data = bus.read_i2c_block_data(QMC5883L_ADDR, 0x00, 6)
    x = data[0] | data[1] << 8
    y = data[2] | data[3] << 8
    z = data[4] | data[5] << 8
    return x, y, z

# Inicializar el sensor
init_sensor()

# Calibración
minX = minY = 32767
maxX = maxY = -32768
print("Mueva el sensor en todas las direcciones para calibrar...")
time.sleep(3)
for i in range(300):
    x, y, z = leer_sensor()
    minX = min(minX, x)
    maxX = max(maxX, x)
    minY = min(minY, y)
    maxY = max(maxY, y)
    time.sleep(0.05)
print("Calibración completada")

# Bucle principal
while True:
    x, y, z = leer_sensor()

    # Normalizar valores
    x = int((x - minX) * (32767 - (-32768)) / (maxX - minX) + (-32768))
    y = int((y - minY) * (32767 - (-32768)) / (maxY - minY) + (-32768))

    # Calcular ángulo
    heading = math.atan2(y, x)
    if heading < 0:
        heading += 2 * math.pi
    heading = heading * 180 / math.pi

    print("Ángulo: {:.2f} grados".format(heading))
    time.sleep(0.5)
