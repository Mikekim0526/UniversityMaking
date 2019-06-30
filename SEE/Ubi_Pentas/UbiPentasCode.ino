#include <BlynkSimpleCurieBLE.h>
#include <CurieBLE.h>
#include <Servo.h>
#include "DHT.h"
//#define BLYNK_USE_DIRECT_CONNECT
#define BLYNK_PRINT Serial

#define DHTPIN 2
#define DHTTYPE DHT11
Servo fan;
DHT dht(DHTPIN, DHTTYPE);

char auth[] = "bb3b350156d145c483bad4c4d255f44c";

BLEPeripheral  blePeripheral;

int fanSpeed = 0;
void setup(){
  Serial.begin(9600);
  dht.begin();
  fan.attach(9);

  delay(1000);

  blePeripheral.setLocalName("Ubi");
  blePeripheral.setDeviceName("Ubi");
  blePeripheral.setAppearance(384);
  Blynk.begin(blePeripheral, auth);
  blePeripheral.begin();

  Serial.println("Waiting for connections...");
}

void loop(){
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
BLYNK_WRITE(13) {
  fanSpeed = param.asInt();
  /*if (fanSpeed==1){
    fan.write(115);
  } else if(fanSpeed==2){
    fan.write(123);
  } else if(fanSpeed==3){
    fan.write(132);
  } else{
    fan.write(0);
  }*/
  fan.write(fanSpeed);
}
BLYNK_READ(10) {
  Blynk.virtualWrite(10, fanSpeed);
}
