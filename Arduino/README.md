# Brujula Digital

Este documento surge por la necesidad de cambiar la lectura del magnetómetro de la Raspberry Pi a un Arduino UNO. También se cambió el módulo GY-87 que incluye un MPU6050 y un magnetómetro HMC5883 por un QMC5883L que funciona en la dirección I2C 0x0D.

## Requisitos

- Arduino UNO
- Arduino IDE
- Sensor QMC5883L

## Compatibilidad

Este programa sólo funciona en Arduino UNO. Se probó su compatibilidad sin bibliotecas dedicadas al sensor, usando sólo manejo de registros con Wire.h en Raspberry Pi, ESP32 Devkit V1 y ESP32 Wroom.

## Circuito de conexión

Se realizó la siguiente conexión entre el sensor y el Arduino UNO.

QMC5883L    Arduino UNO
VCC-------> 5V
GND-------> GND
SDA-------> SDA
SCL-------> SCL

## Obtener valores de calibración

Luego de realizar la conexión anterior, carga en el Arduino UNO el programa llamado `Calibración2.ino` para obtener los valores de lectura del sensor.

Este programa entrará en modo lectura durante 30 segundos luego de iniciar. Durante este periodo, deberás mover el sensor suavemente en todos los ejes que muestra la serigrafía de sensor. Esto obtendrá los valores maximos y mínimos registrados por el sensor.

La lectura se realiza cada 100ms, lo que debes considerar en la velocidad de los movimientos que realizas y anticipar dichos movimientos para que puedas registrar movimiento en todos los ejes del magnetómetro.

Cuando hayas terminado, el monitor serial de Arduino IDE mostrará los valores máximos y mínimos. El programa se comunica a 115200 baudios, por lo que debes tener configurado el monitor serial a esa velocidad.

En caso de que te equivoques, puedes presionar el boton de reset del Arduino UNO y comenzar de nuevo.

Guarda esos valores, pues se usarán en el siguiente programa. En mi caso, los valores registrados fueron los siguientes.

```
minX: -963
maxX: 1080
minY: 0
maxY: 2582
```
## Lectura calibrada

Una vez que has obtenido los valores de calibración para tu sensor, abre el programa llamado `qmc5883l.ino` y coloca dichos valores en la sección llamada *Valores de calibración preestablecidos*.

Carga el progama al arduino.

Este programa enviará los valores de ángulo detectado via USB. 

Conecta el calbe USB del Arduino UNO a la Raspberry Pi para continuar con el proceso.

