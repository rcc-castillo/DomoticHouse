#include "Lights.h"

Lights::Lights(int pin, const String &name) : Device(pin, name) {
    _pin = pin;
    _name = name;
    init();
}

void Lights::init() {
    pinMode(_pin, OUTPUT);
    _lightsState = "off";
    set("", _lightsState);
}

String Lights::get(const String &deviceElement) {
    if (deviceElement.equals("State")) return _lightsState;
    else return "No se pudo obtener la información del dispositivo";
}

void Lights::set(const String &deviceElement, const String &data) {
    if (deviceElement.equals("State")){
        _lightsState = data;
        if (data.equals("on")) digitalWrite(_pin, HIGH);
        else if (data.equals("off")) digitalWrite(_pin, LOW);
    }
}

void Lights::handleProgrammedCommand(const String &command, int currentHour, int currentMinute) {}
