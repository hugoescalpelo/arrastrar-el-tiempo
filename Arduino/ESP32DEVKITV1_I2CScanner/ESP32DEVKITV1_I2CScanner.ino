#include <Wire.h>

void setup() {
  Wire.begin(); // Inicia el bus I2C
  Serial.begin(115200); // Inicia la comunicación serial a 115200 baudios
  while (!Serial); // Espera a que la consola serial esté lista
  Serial.println("\nI2C Scanner");

  byte error, address;
  int nDevices;

  Serial.println("Scanning...");

  nDevices = 0;
  for (address = 1; address < 127; address++ ) {
    // El ESP32 DevKit V1 utiliza 7 bits para la dirección, por lo que recorremos de 0x01 a 0x7F
    Wire.beginTransmission(address);
    error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("I2C device found at address 0x");
      if (address < 16) {
        Serial.print("0");
      }
      Serial.print(address, HEX);
      Serial.println("  !");

      nDevices++;
    } else if (error == 4) {
      Serial.print("Unknown error at address 0x");
      if (address < 16) {
        Serial.print("0");
      }
      Serial.println(address, HEX);
    }
  }
  if (nDevices == 0) {
    Serial.println("No I2C devices found\n");
  } else {
    Serial.println("done\n");
  }
}

void loop() {
  // No necesitamos hacer nada aquí
}
