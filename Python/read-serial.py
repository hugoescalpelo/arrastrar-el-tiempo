import serial
import time

def calcular_direccion(angulo):
    if 315 <= angulo <= 360 or 0 <= angulo < 45:
        return 'N'
    elif 45 <= angulo < 135:
        return 'E'
    elif 135 <= angulo < 225:
        return 'S'
    else:
        return 'W'

# Este puerto puede variar dependiendo de tu configuración de Raspberry Pi
puerto_serial = '/dev/ttyS0'  # Cambia esto según tu configuración de Raspberry Pi

while True:
    try:
        with serial.Serial(puerto_serial, 115200, timeout=1) as ser:
            if ser.is_open:
                print("Dispositivo conectado.")
                while True:
                    linea = ser.readline()
                    if linea:
                        angulo = float(linea.decode().strip())
                        direccion = calcular_direccion(angulo)
                        print(f"Ángulo: {angulo}, Dirección: {direccion}")
    except serial.SerialException:
        print("Dispositivo no conectado o desconectado. Reintentando...")
        time.sleep(1)  # Esperar un poco antes de reintentar
