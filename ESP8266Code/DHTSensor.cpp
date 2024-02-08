#include "DHTSensor.h"

DHTSensor::DHTSensor(int pin, const String &name) : Device(pin, name) {
    _pin = pin;
    _name = name;
    init();
}

void DHTSensor::init() {
    _dht = new DHT(_pin, DHT11);
    _dht->begin();
}

String DHTSensor::get(const String &deviceElement) {
    if (deviceElement.equals("Temperature")) return String(getTemperature());
    else if (deviceElement.equals("Humidity")) return String(getHumidity());
    else return "No se pudo obtener la información del dispositivo";
}

float DHTSensor::getTemperature() {
    float temperature = _dht->readTemperature();
    if (isnan(temperature)) {
        return -999;
    }
    return roundf(temperature * 100) / 100;
}

float DHTSensor::getHumidity() {
    float humidity = _dht->readHumidity();
    if (isnan(humidity)) {
        return -999;
    }
    return humidity;
}

void DHTSensor::set(const String &deviceElement, const String &data) {}

void DHTSensor::handleProgrammedCommand(const String &command, int currentHour, int currentMinute) {}
