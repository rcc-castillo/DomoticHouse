#include "Room.h"

Room::Room() {
}

Room::Room(String name, int lightPin, int blindsPin, int airEnablePin, int airSpeedPin) {
    _name = name;
    _lightPin = lightPin;
    _blindsPin = blindsPin;
    _airEnablePin = airEnablePin;
    _airSpeedPin = airSpeedPin;
    initializeLight();
    initializeBlinds();
    initializeAir();
}

String Room::getName() {
    return _name;
}

void Room::initializeLight() {
    pinMode(_lightPin, OUTPUT);  // Configurar el pin del LED como salida
    digitalWrite(_lightPin, HIGH);  // Apagar el LED al inicio
}

void Room::setLightStatus(String status) {
    if (status == "on") {
        digitalWrite(_lightPin, LOW);
    }
    else if (status == "off")
    {
        digitalWrite(_lightPin, HIGH);
    }
}

void Room::initializeBlinds() {
    _blindsServo.attach(_blindsPin);  
    _blindsServo.write(0);
}

void Room::setBlindsStatus(String status) {
  if (status == "up") _blindsServo.write(180);
  else if (status == "down") _blindsServo.write(0);
}

void Room::initializeAir() {
  pinMode(_airEnablePin, OUTPUT);
  pinMode(_airSpeedPin, OUTPUT);
  setAirStatus("off");
}

void Room::setAirStatus(String status) {
    if (status == "on") digitalWrite(_airEnablePin, LOW);
    else if (status == "off") digitalWrite(_airEnablePin, HIGH);
}

void Room::setAirSpeed(String speed) {
    if (speed == "baja") digitalWrite(_airSpeedPin, 85);
    else if (speed == "media") digitalWrite(_airSpeedPin, 170);
    else if (speed == "alta") digitalWrite(_airSpeedPin, 255);
}