import serial
import time
import pygame
from pygame import mixer

def calcular_direccion(angulo):
    if 315 <= angulo <= 360 or 0 <= angulo < 45:
        return 'N'
    elif 45 <= angulo < 135:
        return 'E'
    elif 135 <= angulo < 225:
        return 'S'
    else:
        return 'W'

def reproducir_audio(direccion_actual, direccion_anterior):
    if direccion_actual != direccion_anterior:
        mixer.music.fadeout(5000) # Crossfade de 5 segundos
        time.sleep(5) # Esperar a que termine el crossfade
        mixer.music.load(f'audio0{audios[direccion_actual]}.mp3')
        mixer.music.play(-1) # Reproducir indefinidamente

# Asignar un archivo de audio a cada dirección
audios = {'N': '1', 'E': '2', 'S': '3', 'W': '4'}

# Inicializar pygame mixer
pygame.init()
mixer.init()
mixer.music.set_volume(0.7) # Ajustar el volumen si es necesario

puerto_serial = '/dev/ttyS0'  # Cambia esto según tu configuración de Raspberry Pi
direccion_anterior = None

while True:
    try:
        with serial.Serial(puerto_serial, 115200, timeout=1) as ser:
            if ser.is_open:
                print("Dispositivo conectado.")
                while True:
                    linea = ser.readline()
                    if linea:
                        angulo = float(linea.decode().strip())
                        direccion_actual = calcular_direccion(angulo)
                        print(f"Ángulo: {angulo}, Dirección: {direccion_actual}")
                        reproducir_audio(direccion_actual, direccion_anterior)
                        direccion_anterior = direccion_actual
    except serial.SerialException:
        print("Dispositivo no conectado o desconectado. Reintentando...")
        time.sleep(1)  # Esperar un poco antes de reintentar
