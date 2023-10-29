#include "Room.h"

Room::Room() {
    _name = "";
    _lightPin = 0;
    _lightStatus = false;
}

Room::Room(String name, int lightPin) {
    _name = name;
    _light.pin = lightPin;
    _light.status = false; // Inicializamos el estado de la luz en apagado
}

String Room::getName() {
    return _name;
}

int Room::getLightPin() {
    return _light.pin;
}

void Room::setLightStatus(uint8_t status) {
    digitalWrite(_light.pin, status);
}

void Room::initializeLight() {
    pinMode(_light.pin, OUTPUT);  // Configurar el pin del LED como salida
    digitalWrite(_light.pin, HIGH);  // Apagar el LED al inicio
}
