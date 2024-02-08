#include "Blinds.h"

Blinds::Blinds(int pin, const String &name) : Device(pin, "Blinds") {
    _pin = pin;
    _name = name;
    init();
}

void Blinds::init() {
    _blindsServo.attach(_pin, 500, 2500);
    _blindsState = "down";
    set("State", _blindsState);
}

String Blinds::get(const String &deviceElement) {
    if (deviceElement.equals("State")) return _blindsState;
    else return "No se pudo obtener la información del dispositivo";
}

void Blinds::set(const String &deviceElement, const String &data) {
    if (deviceElement.equals("State")){
        _blindsState = data;
        if (data.equals("up")) _blindsServo.write(179);
        else if (data.equals("down")) _blindsServo.write(0);
    }
}

void Blinds::handleProgrammedCommand(const String &command, int currentHour, int currentMinute) {}
