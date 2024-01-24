# Programa en Python

En este documento encontrarás instrucciones para correr el programa de Python.

## Configuración de Raspberry Pi

### Activar I2C
Este programa hace uso del sensor GY-87, el cual se comunica con I2C. Para que sea posible, es necesario activarlo en las interfases de la Raspberry Pi
- Ejecuta el comando `sudo raspi-config`
- Desplazate a `Interface Options`
- Selecciona `I2C`
- Selecciona la opción `Yes`
- Reinicia la Raspberry con el comando `sudo reboot`

### Instalar Python
Primero comprueba que Python se encuentra instalado, corre el siguiente comando en una terminal.

```
python --version
```
 En este caso el resultado fue el siguiente:

```
Python 3.9.2
```
En caso de no tener python instalado, corre el siguiente programa. Este comando requiere conexión a Internet.
```
sudo apt-get update
sudo apt-get install python3
```
## Instalación de bibliotecas

- smbus (i2c)

## Configuración de audios

## Circuito

## Correr el programa

## Script de inicio

## Pruebas

Las pruebas que se presentan a continuación son una herramienta para comprobar que todos los sistemas funcionan. También tienen como propósito que conozcas que información se requiere para poder hacer cambios de hardware o software.

En el siguiente documento puedes encontrar las instrucciones para correr las pruebas necesarias para que todo en el programa funcione.
- [Test de brujula digital](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Python/magnetometer.md)