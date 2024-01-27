#include <Wire.h>

#define QMC5883L_ADDR 0x0D

// Valores de calibración preestablecidos
const int minX = -963;
const int maxX = 1080;
const int minY = 0;
const int maxY = 2582;

void setup() {
  Serial.begin(115200); // Configura la velocidad del puerto serial a 115200 baudios
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
}

void loop() {
  int x, y, z;
  leerSensor(&x, &y, &z);

  // Normalizar los valores del sensor
  x = map(x, minX, maxX, -32768, 32767);
  y = map(y, minY, maxY, -32768, 32767);

  // Calcular el ángulo
  float angulo = calcularAngulo(x, y);

  // Enviar el ángulo por el puerto serial
  //Serial.print("Angulo: ");
  Serial.println(angulo);

  delay(500); // Espera 500 milisegundos antes de la siguiente lectura
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

float calcularAngulo(int x, int y) {
  float heading = atan2(y, x);
  if (heading < 0) heading += 2 * PI;
  return heading * 180 / PI;
}
