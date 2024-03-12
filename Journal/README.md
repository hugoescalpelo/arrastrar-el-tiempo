# Journal

## 2024-01-14

Tuve la junta inicial con Sué, donde me explicó la mecánica de funcionamiento.

## 2024-01-19

Ordené el transmisor de audio en Amazon. [Pomya Transmisor FM de 500 MW](https://www.amazon.com.mx/dp/B0CC2SCDXH)

## 2024-01-20

Llegó el transmisor.

Hice una prueba. Conecté la antena al transmisor, conecté una bateria para celular al transmisor para almentarlo, conecté un auxiliar para hacer una prueba de transmisión, la cual fué exitosa.

Logré transmitir audio con buena calidad en la distancia máxima de mi departamento, que son como 6 metros de distancia. Es suficiente para los efectos de la pieza de Sué y el espacio del performance.

## 2024-01-21

Comencé por crear el repositorio.

[Arrastrar el tiempo - GitHub](https://github.com/hugoescalpelo/arrastrar-el-tiempo)

---
Creé el diagrama general.

![](https://github.com/hugoescalpelo/arrastrar-el-tiempo/blob/main/Im%C3%A1genes/Diagrama%20general%20Arrastrar%20el%20Tiempo.png?raw=true)

---
Comenzaré por hacer pruebas de alimentación únicamente con la bateria de celular y cables USB.

---
Pues ya conecté todo a una pila y funcionó como esperaba. 

La siguiente parte es hacer que cambien los audios dependiendo de cómo se girla la mesa. Le pregunté a Sue cómo va y parece se se cambiará por una improvisación de Mau. En ese caso ya terminé. Pero bueno, esperaré la respuesta.

Puede verse la primera prueba acá.

[Primer prueba del transmisor de audio](https://www.instagram.com/p/C2YZ9prOXzU/)

## 2024-01-23

Hoy tuve una junta con Sué, donde me confirmó que el comportamiento corresponde a audios que se reproducen fundidos cuando se mueve la mesa con el sensor.

---
Agregé los archivos de audio que Sué me mandó por whatsapp.

---
He creado los diagramas y realizado la documentación.

## 2024-01-24

He creado un programa de prueba para garantizar que funciona la brújula digital.

---
Traté de completar un programa que reprodujera los audios y leyera la brujula pero no lo logré.

---
He notado que el motivo por el cual el programa no cambia los audios es porque se daño la brujula digital. En este momento he comprado otra. Estoy a la espera de la entrega.

## 2024-01-25

Ha llegado el sensor

## 2024-01-26

He soldado el sensor, estoy por probarlo.

## 2024-01-26 Post Mortem

El sensor GY-87 no funcionó de ninguna forma en la Raspberry Pi, ESP32 Devkit V1, ESP32 Wroom ni Arduino UNO. El Escanner I2C no lo reporto en la dirección 0x1E.

Fui a comprar otro a una tienda diferente. Compre un HMC5883L. Luego de soldarlo y tratar de programarlo, no encontré forma alguna de hacerlo funcionar en la Raspberry Pi, ESP32 Devkit V1, ESP32 Wroom ni Arduino UNO al igual que el anterior.

Cuando usaba el I2C scanner no logré encontrarlo en la dirección en 0x1E al igual que los anteriores, pero lo encontré en 0x0D. 

Probando todas las bibliotecas disponibles en la IDE de Arduino, logré encontrar que la siguiente tenia un device identifier

https://github.com/LiquidCGS/FastIMU

Este dispositivo me dijo que el sensor en realidad era un QMC5883L, por lo que se advierte que el código funciona exclusivamente con el sensor seleccionado y que otros sensores pueden no funcionar con el mismo código.

Una vez que logré identificarlo, pude generar un programa que lo leyera en Arduino UNO, probé el mismo programa con los mismos registros en la Raspberry Pi y los ESP32 y no fue posible leerlo. Por eso decidí conectar por USB el Arduino UNO a la Raspberry Pi y modificar la lista de componentes.

Luego de hacer algunas lecturas simples, continué con el programa en la raspberry pi y logré detonar los audios, pero noté que las lecturas no tenían el rango completo y que los ángulos solo iban de 45° a 130°, por lo que regresé al programa de Arduino a buscar opciones de calibración.

Encontré que la biblioteca FastIMU incluye un programa que toma las lecturas luego de la calibración. El programa tiene un proceso de calibración de 30 segundos donde hace muchas lecturas y toma los rangos del magnetómetro, este programa quedó en el repositorio como "Calibracion.ino". Luego los usa para dar el rango completo de 0° a 360°. Dejé ese programa y continué en Raspberry Pi.

Ya en Raspberry Pi noté que no se quedaban guardadas las calibraciones, por lo que regresé a Arduino UNO e hice un programa que diera como resultado los rangos leídos, este programa quedó llamado "Calibracion2.ino". Luego de varias pruebas de calibración, obtuve los siguientes valores de calibración:
```
minX: -963
maxX: 1080
minY: 0
maxY: 2582
```


El programa "Calibración2.ino" fue modificado para que devolviera estos valores. Es **MUY IMPORTANTE** realizar esta calibración con cada sensor nuevo, puede variar con la construcción.

Luego generé el programa "qmc5883l" para que tomara dichos valores y devolviera por serial el ángulo considerando los valores de calibracion. Este fue el programa que quedó en el Arduino UNO.

Volví a la Raspberry Pi y tomé el valor de lectura del sensor. Este programa fue exitoso en el sentido de que hace el crossfade para reproducir el audio, pero tenía el problema de que al cambiar la posición del sensor el ruido del movimiento podía hacer que un audio equivocado se reprodujerea algunos segundos.

Se puede ver en el siguiente video.

https://www.instagram.com/p/C2lr7G1uFEF/

Con esto cerré el día

## 2024-01-27 Post Mortem

Es el día de la entrega. Me desperté temprano a agregar una secuencia que sólo cambiara el audio reproducido hasta el momento que se detectan 5 lecturas indicando el mismo punto cardinal. Esto reduce las fallas al mover el sensor pero hace que tengan que pasar 5 segundos al cambiar la posición para que se active el audio correspondiente.

Luego di de alta el programa de Python como servicio para que se arrancara automáticamente. No funcionó por mas que intenté ajustarlo. Usé como guía el Ubuntu quickie que generé en el siguiente repositorio.

[Startup-Script](https://github.com/hugoescalpelo/ubuntu-quickies/blob/main/Startup-script/startup-script.md)

Como solución llevé una pantalla Touch para que Sué arrancara el programa, pero al llegar y conectar todo, funcionó el arranque automático.

Se puede ver en el siguiente video.

https://www.instagram.com/p/C2nRRE1Okpn/

Conecté todo a un Power Bank de 20000MAh para garantizar que todo funcionaría durante la presentación.

Con esto cierro el desarrollo. Quedo a la espera de material y observaciones de Sué para complementar el journal.

## 2024-01-31

Complementé el Journal. Espero material de registro de Sué.

---
He completado la documentación del proyecto.

## 2024-03-11

Se ha agregado un documento de excel describiendo el material usado para la presentación y sus costos. En el mismo documento se detalla el material minimo recomendado para reproducir el proyecto.