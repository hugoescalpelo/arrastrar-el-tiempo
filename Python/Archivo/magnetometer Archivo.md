## Pruebas de brujula digital

Para correr este programa necesitas instalar las bilbotecas `smbus`.
```
sudo apt-get update
sudo apt-get install python3-smbus
sudo pip3 install smbus2
```
Este programa requiere [Python y PIP instalados](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Python/README.md#instalar-python).

Para correr este programa ejecuta el siguiente comando.
```
python ~/Documents/GitHub/arrastrar-el-tiempo/Python/magnetometer.py
```

Este programa muestra el ángulo al que apunta la brujula digital y determina si es norte, sur, este u oeste.

Para detener este programa presiona Ctrl+C

Esta información es necesaria para el programa principal, ya que la orientación se usa para detonar distintos audios.