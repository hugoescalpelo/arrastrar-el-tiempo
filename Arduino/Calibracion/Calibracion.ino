#include <Wire.h>

#define QMC5883L_ADDR 0x0D

// Variables para almacenar los valores mínimos y máximos
int minX, maxX, minY, maxY;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Inicializar QMC5883L
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
  delay(3000); // Tiempo para mover el sensor en varias orientaciones

  // Calibración
  for (int i = 0; i < 300; i++) {
    int x, y, z;
    leerSensor(&x, &y, &z);

    if (x < minX) minX = x;
    if (x > maxX) maxX = x;
    if (y < minY) minY = y;
    if (y > maxY) maxY = y;

    delay(50);
  }
  Serial.println("Calibración completada");
}

void loop() {
  int x, y, z;
  leerSensor(&x, &y, &z);

  // Normalizar valores
  x = map(x, minX, maxX, -32768, 32767);
  y = map(y, minY, maxY, -32768, 32767);

  // Calcular ángulo
  float heading = atan2(y, x);
  if (heading < 0) heading += 2 * PI;
  heading = heading * 180 / PI;

  Serial.print("Ángulo: ");
  Serial.print(heading);
  Serial.println(" grados");

  delay(500);
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
