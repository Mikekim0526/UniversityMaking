#include <BlynkSimpleCurieBLE.h>
#include <CurieBLE.h>
#include "DHT.h"

//#define BLYNK_USE_DIRECT_CONNECT
#define BLYNK_PRINT Serial

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

char auth[] = "bb3b350156d145c483bad4c4d255f44c";

BLEPeripheral  blePeripheral;

int fanSpeed = 0;
void setup()
{
  // Debug console
  Serial.begin(9600);
  dht.begin();


  delay(1000);

  blePeripheral.setLocalName("Ubi");
  blePeripheral.setDeviceName("Ubi");
  blePeripheral.setAppearance(384);
  Blynk.begin(blePeripheral, auth);
  blePeripheral.begin();

  Serial.println("Waiting for connections...");
}

void loop()
{
  //  float humidity = dht.readHumidity();
  //  float temperature = dht.readTemperature();

  blePeripheral.poll();
  Blynk.run();
}

BLYNK_READ(1) {
  float humidity = dht.readHumidity();
  Blynk.virtualWrite(1, humidity);
}
BLYNK_READ(2) {
  float temperature = dht.readTemperature();
  //  Blynk.virtualWrite(0, temperature);
  Blynk.virtualWrite(2, temperature);
}
BLYNK_WRITE(10) {
  fanSpeed = param.asInt();
}
BLYNK_READ(3) {
  Blynk.virtualWrite(3, fanSpeed);
}
