#include "Irrigation.h"

Irrigation::Irrigation(int pin, const String &name) : Device(pin, name) {
    _pin = pin;
    _name = name;
    init();
}

void Irrigation::init() {
    pinMode(_pin, OUTPUT);
    _irrigationState = "off";
    setIrrigationState(_irrigationState);
}

String Irrigation::get(const String &deviceElement) {
    if (deviceElement.equals("State")) return _irrigationState;
    else if (deviceElement.equals("StartTime")) return getIrrigationStartTime();
    else if (deviceElement.equals("EndTime")) return getIrrigationEndTime();
    else return "No se pudo obtener la información del dispositivo";
}

void Irrigation::set(const String &deviceElement, const String &data) {
    if (deviceElement.equals("State")) setIrrigationState(data);
    else if (deviceElement.equals("StartTime")) setIrrigationStartTime(data);
    else if (deviceElement.equals("EndTime")) setIrrigationEndTime(data);
}

String Irrigation::getIrrigationStartTime() {
    return std::get<0>(_irrigationStartTime) + ":" + std::get<1>(_irrigationStartTime);
}

String Irrigation::getIrrigationEndTime() {
    return std::get<0>(_irrigationEndTime) + ":" + std::get<1>(_irrigationEndTime);
}

void Irrigation::setIrrigationState(const String &data) {
    _irrigationState = data;
    if (data.equals("on")) _irrigationEnabled = true;
    else if (data.equals("off")) _irrigationEnabled = false;
}

void Irrigation::setIrrigationStartTime(const String &data) {
    int hour = data.substring(0, 2).toInt();
    int minute = data.substring(3, 5).toInt();
    _irrigationStartTime = std::make_tuple(hour, minute);
}

void Irrigation::setIrrigationEndTime(const String &data) {
    int hour = data.substring(0, 2).toInt();
    int minute = data.substring(3, 5).toInt();
    _irrigationEndTime = std::make_tuple(hour, minute);
}

void Irrigation::handleProgrammedCommand(const String &command, int currentHour, int currentMinute) {
    if (!command.equals("Irrigate")) return;
    Serial.println(_irrigationEnabled);
    if (!_irrigationEnabled) {
        digitalWrite(_pin, LOW);
        return;
    }
    int startHour = std::get<0>(_irrigationStartTime);
    int startMinute = std::get<1>(_irrigationStartTime);
    int endHour = std::get<0>(_irrigationEndTime);
    int endMinute = std::get<1>(_irrigationEndTime);

    bool isWithinTimeRange = (currentHour > startHour || (currentHour == startHour && currentMinute >= startMinute)) &&
            (currentHour < endHour || (currentHour == endHour && currentMinute < endMinute));

    if (endHour > startHour || (endHour == startHour && endMinute > startMinute)) {
        Serial.println("isWithinTimeRange: " + String(isWithinTimeRange));
        Serial.println("digitalWrite: " + String(isWithinTimeRange ? "HIGH" : "LOW"));
        digitalWrite(_pin, isWithinTimeRange ? HIGH : LOW);
    }

    else if (endHour < startHour || (endHour == startHour && endMinute < startMinute)) {   
        Serial.println("isWithinTimeRange: " + String(isWithinTimeRange));
        Serial.println("digitalWrite: " + String(isWithinTimeRange ? "HIGH" : "LOW"));
        digitalWrite(_pin, isWithinTimeRange ? LOW : HIGH);
    }
    else if (endHour == startHour && endMinute == startMinute) {
        Serial.println("LOW");
        digitalWrite(_pin, LOW);
    }
}
