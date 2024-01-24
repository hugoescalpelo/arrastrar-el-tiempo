import smbus
import math
import pygame
import os
import time

# Inicializa Pygame para la reproducción de audio
pygame.mixer.init()

# Configuración del bus I2C para el HMC5883L
bus = smbus.SMBus(1)
address = 0x1E

def read_sensor(addr):
    data = bus.read_i2c_block_data(addr, 0x03, 6)
    x = data[0] * 256 + data[1]
    if x > 32767:
        x -= 65536
    y = data[4] * 256 + data[5]
    if y > 32767:
        y -= 65536
    z = data[2] * 256 + data[3]
    if z > 32767:
        z -= 65536
    return x, y, z

def calculate_heading(x, y):
    heading = math.atan2(y, x)
    if heading < 0:
        heading += 2 * math.pi
    return math.degrees(heading)

def get_cardinal(heading):
    if heading >= 45 and heading < 135:
        return 'E'
    elif heading >= 135 and heading < 225:
        return 'S'
    elif heading >= 225 and heading < 315:
        return 'W'
    else:
        return 'N'

# Configura el HMC5883L
bus.write_byte_data(address, 0, 0b01110000)
bus.write_byte_data(address, 1, 0b00100000)
bus.write_byte_data(address, 2, 0b00000011)

audio_files = {
    'N': 'Audio/audio01.mp3',
    'E': 'Audio/audio02.mp3',
    'S': 'Audio/audio03.mp3',
    'W': 'Audio/audio04.mp3'
}

current_cardinal = None
current_channel = None

while True:
    x, y, z = read_sensor(address)
    heading = calculate_heading(x, y)
    cardinal = get_cardinal(heading)

    if cardinal != current_cardinal:
        if current_channel:
            current_channel.fadeout(1000)
        current_channel = pygame.mixer.Channel(0)
        current_channel.play(pygame.mixer.Sound(audio_files[cardinal]), loops=-1)
        current_cardinal = cardinal

    time.sleep(0.1)
