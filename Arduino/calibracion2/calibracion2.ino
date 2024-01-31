#include <Wire.h>

#define QMC5883L_ADDR 0x0D

// Variables para almacenar los valores mínimos y máximos
int minX, maxX, minY, maxY;

void setup() {
  Serial.begin(115200); // Velocidad de comunicación configurada a 115200 baudios
  Wire.begin();

  // Configuración inicial del QMC5883L
  Wire.beginTransmission(QMC5883L_ADDR);
  Wire.write(0x0B);
  Wire.write(0x01);
  Wire.endTransmission();

  Wire.beginTransmission(QMC5883L_ADDR);
  Wire.write(0x09);
  Wire.write(0x1D);
  Wire.endTransmission();

  // Inicializar valores mínimos y máximos
  minX = minY = 32767;
  maxX = maxY = -32768;

  Serial.println("Mueva el sensor en todas las direcciones para calibrar...");
}

void loop() {
  calibrarSensor();
  delay(100); // Retraso de 100 ms para 10 lecturas por segundo
}

void calibrarSensor() {
  int x, y, z;
  leerSensor(&x, &y, &z);

  Serial.print("X: "); Serial.print(x);
  Serial.print(" Y: "); Serial.print(y);
  Serial.print(" Z: "); Serial.println(z);

  if (x < minX) minX = x;
  if (x > maxX) maxX = x;
  if (y < minY) minY = y;
  if (y > maxY) maxY = y;

  // Imprimir valores de calibración tras 30 segundos (300 lecturas)
  static int contador = 0;
  if (++contador >= 300) {
    Serial.println("Calibración completada");
    Serial.print("minX: "); Serial.println(minX);
    Serial.print("maxX: "); Serial.println(maxX);
    Serial.print("minY: "); Serial.println(minY);
    Serial.print("maxY: "); Serial.println(maxY);

    // Detener el programa
    while(true) {}
  }
}

void leerSensor(int *x, int *y, int *z) {
  Wire.beginTransmission(QMC5883L_ADDR);
  Wire.write(0x00);
  Wire.endTransmission();

  Wire.requestFrom(QMC5883L_ADDR, 6);
  if (6 <= Wire.available()) {
    *x = Wire.read() | Wire.read() << 8;
    *y = Wire.read() | Wire.read() << 8;
    *z = Wire.read() | Wire.read() << 8;
  }
}

