#include <Wire.h>

// Dirección I2C del QMC5883L
#define QMC5883L_ADDR 0x0D

// Registros del QMC5883L
#define QMC5883L_X_LSB 0x00
#define QMC5883L_X_MSB 0x01
#define QMC5883L_Y_LSB 0x02
#define QMC5883L_Y_MSB 0x03
#define QMC5883L_Z_LSB 0x04
#define QMC5883L_Z_MSB 0x05
#define QMC5883L_STATUS 0x06
#define QMC5883L_TEMP_LSB 0x07
#define QMC5883L_TEMP_MSB 0x08
#define QMC5883L_CONFIG 0x09
#define QMC5883L_CONFIG2 0x0A
#define QMC5883L_RESET 0x0B
#define QMC5883L_CHIP_ID 0x0D

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Inicializar QMC5883L
  Wire.beginTransmission(QMC5883L_ADDR);
  Wire.write(QMC5883L_CONFIG);
  Wire.write(0x01);
  Wire.endTransmission();
}

void loop() {
  int16_t x, y, z;
  float heading;

  // Leer datos del QMC5883L
  Wire.beginTransmission(QMC5883L_ADDR);
  Wire.write(QMC5883L_X_LSB);
  Wire.endTransmission();
  
  Wire.requestFrom(QMC5883L_ADDR, 6);
  if (6 <= Wire.available()) {
    x = Wire.read() | Wire.read() << 8;
    y = Wire.read() | Wire.read() << 8;
    z = Wire.read() | Wire.read() << 8;
  }

  // Calcular el ángulo (heading)
  heading = atan2(y, x);
  if (heading < 0) {
    heading += 2 * PI;
  }
  heading = heading * 180/PI;

  // Imprimir el ángulo
  Serial.print("Ángulo: ");
  Serial.print(heading);
  Serial.println(" grados");

  delay(500);
}
