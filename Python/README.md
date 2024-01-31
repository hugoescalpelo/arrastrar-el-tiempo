# Detonado de audios

En este documento están las instrucciones para asegurarse de que la sección de audio funciona.

## Requisitos

### Python

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

### PySerial

Esta biblioteca es usada por Python para comunicarse con le Arduino UNO y obtener el valor de la lectura de la brujula digital. Para instalar esta biblioteca ejecuta los siguientes comandos.
```
sudo apt-get update
sudo pip install pyserial
```
### PyGame

Esta biblioteca es usada por Python para detonar los audios. Para instalar esta biblioteca ejecuta los siguientes comandos.
```
sudo apt-get update
sudo pip install pygame
```

### Permite el acceso al usuario al grupo dialout

Para que tu usuario de linux tenga permisos para leer puertos seriales, ejecuta el siguiente comando

```
sudo usermod -a -G dialout usuario
```

Reinicia el sistema

### Determina el puerto del Arduino UNO

De forma predeterminada, el arduino UNO se registra en el puerto `/dev/ttyACM0`, aunque en ocaciones puede variar. Ejecuta el siguiente comando para comprobar que en verdad se encuentra en dicho puerto.

```
dmesg | grep tty
```
En caso de que este en otro puerto, por ejemplo en `/dev/ttyACM1` o en `/dev/ttyUSB0`, deberás ajustar el código del programa llamado`arrastrar-el-tiempo-5.py` en la linea 30.

## Prueba el programa
