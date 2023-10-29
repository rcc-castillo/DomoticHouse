#include "Room.h"

Room::Room() {
}

Room::Room(String name, int lightPin) {
    _name = name;
    _lightPin = lightPin;
    initializeLight();
}

String Room::getName() {
    return _name;
}

int Room::getLightPin() {
    return _lightPin;
}

void Room::setLightStatus(uint8_t status) {
    Serial.println("Cambiando estado de luz a " + String(status));
    digitalWrite(_lightPin, status);
}

void Room::initializeLight() {
    pinMode(_lightPin, OUTPUT);  // Configurar el pin del LED como salida
    digitalWrite(_lightPin, HIGH);  // Apagar el LED al inicio
}
