# arrastrar-el-tiempo
Este repositorio es una colaboración con Sué Monserrar Jacome Lugo para el desarrollo de la parte tecnológica de su obra Arrastrar el Tiempo

Este proyecto es una comisión.

Consiste en una mesa móvil con una serie de radios en circulo a su alrededor, tipo reloj, hay una cabeza cubierta de hojas de lechuga en el centro. Es un performance en dos partes.
- Parte 1: Ritual de pelar la lechuga y revelar la cabeza, después cubrirla de polvo. Los radios están alrededor sintonizando estática.
- Parte 2: Se girará la mesa y conforme se gire, el audio cambiará. Esto se hará durante 10 minutos.

Fecha de presentación 27 de enero de 2024

## Material necesario

| Cantidad | Concepto |
|----------|----------|
|1|Transmisor de radio 500mW|
|1|Raspberry Pi 3B+ 2GB|
|1|Brujula Digital QMC5883L|
|1|Arduino UNO|
|1|Bateria 20000MAh|
|1|Cableado|

## Journal

Puedes conocer un diario de desarrollo en el siguiente enlace.
[Journal](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/README.md)

Es muy importante leer el Journal del proyecto para comprender en detalle las dificultades de manejar el magnetómetro. Expreso las peculiaridades del sensor y la necesidad de un proceso previo de calibración personalizada para cada sensor a pesar de que sean del mismo modelo que el del desarrollo inicial.

## Diagramas

Este es el diagrama general de conexiones. 

![](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Im%C3%A1genes/Diagrama%20general%20Arrastrar%20el%20Tiempo.png?raw=true)

## Compatibilidad

Este repositorio tiene como proposito correr en una Raspberry Pi. Es compatible con modelos 3B+ y 4. No se ha probado en 5.

Este repositorio sólo extiende funcionamiento con el sensor magnetómetro QMC5883L ubicado en la dirección I2C 0x0D.

## Instrucciones

Para clonar este repositorio en Raspberry Pi, realiza lo siguiente:
- Instalar Git en Raspberry Pi
    ```
    sudo apt-install git
    ```
- Crear directorio de GitHub y entrar en el
    ```
    mkdir ~\Documents\GitHub
    cd ~\Documents\GitHub
    ```
- Clonar el repositorio
    ```
    git clone https://github.com/hugoescalpelo/arrastrar-el-tiempo.git
    ```
- En caso de que necesites actualziar el repositorio, entra al directorio `arrastrar-el-tiempo` y ejecuta el siguiente comando.
    ```
    git pull
    ```

Para poder hacer funcionar este proyecto se recomienda leer la documentación completa primero.

- [Instalación y arranque automático](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Python/README.md)

En caso de que desees cambiar el hardware, alguna biblioteca o entender cómo funcionan la carga de audios, se recomienda leer la sección de tests.

- [Brujula digital](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Python/magnetometer.md)