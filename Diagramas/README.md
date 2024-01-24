# Diagramas

En este documento encontrarás los diagramas del proyecto.

## Conexión general
Este diagrama esta hecho en Mermaid para MarkDown y es visible en GitHub.
```mermaid
graph TD;
    Tx2[Transmisor FM] --> |BNC| Tx1[Antena]
    Rp[Raspberry Pi] --> |Jack 3.5mm| Tx2
    Bt[Batería] --> |USB| Rp
    Mg[Brújula Digital] --> |I2C| Rp;

    Bt --> |USB-C| Tx2;

    R1[Radio 1] --> |FM| Tx1
    R2[Radio 2] --> |FM| Tx1
    R3[Radio 3] --> |FM| Tx1
    R4[Radio 4] --> |FM| Tx1;
```

## Conexión del sensor

Se usará un sensor GY-87 vía I2C, el cual se representa con la siguiente tabla
```
GY-87   Raspberry Pi
Vcc---->3.3V
GND---->GND
SDA---->GPIO2 (SDA)
SCL---->GPIO3 (SCL)
```
Si tienes duda cuales son los pines de cada sensor, consulta su pinout en este repositorio:

- [Raspberry Pi Pinout](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Im%C3%A1genes/Raspberry%20Pi%203B%2B%20GPIO.png)
- [GY-87 Pinout](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Im%C3%A1genes/GY87%20Pinout.jpg)