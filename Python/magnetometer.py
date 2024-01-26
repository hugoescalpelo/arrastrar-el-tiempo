import smbus
import time
import math

# Dirección I2C del QMC5883L
QMC5883L_ADDR = 0x0D

def init_qmc5883l():
    bus.write_byte_data(QMC5883L_ADDR, 0x0B, 0x01)
    bus.write_byte_data(QMC5883L_ADDR, 0x09, 0x1D)

def read_sensor():
    bus.write_byte_data(QMC5883L_ADDR, 0x00, 0x00)
    data = bus.read_i2c_block_data(QMC5883L_ADDR, 0x00, 6)
    x = data[0] | data[1] << 8
    y = data[2] | data[3] << 8
    z = data[4] | data[5] << 8
    return x, y, z

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def calibrate_sensor():
    minX, maxX, minY, maxY = 32767, -32768, 32767, -32768
    print("Mueva el sensor en todas las direcciones para calibrar...")
    time.sleep(3)  # Tiempo para mover el sensor

    for _ in range(300):
        x, y, z = read_sensor()
        minX, maxX = min(x, minX), max(x, maxX)
        minY, maxY = min(y, minY), max(y, maxY)
        time.sleep(0.05)

    return minX, maxX, minY, maxY

def calculate_heading(x, y):
    heading = math.atan2(y, x)
    if heading < 0:
        heading += 2 * math.pi
    heading = math.degrees(heading)
    return heading

# Inicializar I2C (smbus)
bus = smbus.SMBus(1)  # Usar 0 para modelos antiguos de Raspberry Pi

# Inicializar el sensor QMC5883L
init_qmc5883l()

# Calibrar el sensor
minX, maxX, minY, maxY = calibrate_sensor()
print("Calibración completada")

try:
    while True:
        x, y, z = read_sensor()
        x = map_value(x, minX, maxX, -32768, 32767)
        y = map_value(y, minY, maxY, -32768, 32767)
        heading = calculate_heading(x, y)
        print(f"Ángulo: {heading:.2f} grados")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Programa terminado por el usuario")
