import smbus
import math
import time
from pydub import AudioSegment
from pydub.playback import play
import threading

# Configuración del bus I2C para el HMC5883L
bus = smbus.SMBus(1)
address = 0x1E

def read_sensor(addr):
    data = bus.read_i2c_block_data(addr, 0x03, 6)
    x = (data[0] << 8) + data[1]
    if x > 32767:
        x -= 65536
    y = (data[4] << 8) + data[5]
    if y > 32767:
        y -= 65536
    return x, y

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
    'N': 'audio01.mp3',
    'E': 'audio02.mp3',
    'S': 'audio03.mp3',
    'W': 'audio04.mp3'
}

current_cardinal = None
audio_thread = None

def play_audio(file):
    audio = AudioSegment.from_file(file)
    play(audio)

def audio_player_thread(file):
    global audio_thread
    if audio_thread and audio_thread.is_alive():
        audio_thread.join()
    audio_thread = threading.Thread(target=play_audio, args=(file,))
    audio_thread.start()

while True:
    x, y = read_sensor(address)
    heading = calculate_heading(x, y)
    cardinal = get_cardinal(heading)
    print(f"Dirección del sensor: {cardinal} (Heading: {heading:.2f} grados)")

    if cardinal != current_cardinal:
        current_cardinal = cardinal
        audio_file = audio_files[cardinal]
        print(f"Reproduciendo: {audio_file}")
        audio_player_thread(audio_file)

    time.sleep(1)
