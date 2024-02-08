#include "AirConditioner.h"

AirConditioner::AirConditioner(int enablePin1, int enablePin2, int speedPin, const String &name) : Device(enablePin1, name) {
    _enablePin1 = enablePin1;
    _enablePin2 = enablePin2;
    _speedPin = speedPin;
    _name = name;
    init();
}

void AirConditioner::init() {
    pinMode(_enablePin1, OUTPUT);
    pinMode(_enablePin2, OUTPUT);
    pinMode(_speedPin, OUTPUT);
    _airState = "off";
    _airSpeedState = "baja";
    _airSpeed = 0;
    set("State", _airState);
    set("Speed", _airSpeedState);
}

String AirConditioner::get(const String &deviceElement) {
    if (deviceElement.equals("State")) return _airState;
    else if (deviceElement.equals("Speed")) return _airSpeedState;
    else return "No se pudo obtener la información del dispositivo";
}

void AirConditioner::set(const String &deviceElement, const String &data) {
    if (deviceElement.equals("State")) setAirState(data);
    else if (deviceElement.equals("Speed")) setAirSpeed(data);
}

void AirConditioner::setAirState(const String &data) {
    _airState = data;
    if (data.equals("on")) {
        digitalWrite(_enablePin1, HIGH);
        digitalWrite(_enablePin2, LOW);
    }
    else if (data.equals("off")) {
        digitalWrite(_enablePin1, LOW);
        digitalWrite(_enablePin2, LOW);
    }
}

void AirConditioner::setAirSpeed(const String &data) {
    _airSpeedState = data;
    if (data.equals("baja")) _airSpeed = 85;
    else if (data.equals("media")) _airSpeed = 170;
    else if (data.equals("alta")) _airSpeed = 255;
    analogWrite(_speedPin, _airSpeed);
}

void AirConditioner::handleProgrammedCommand(const String &command, int currentHour, int currentMinute) {}
