#include "Room.h"

Room::Room() {}

Room::Room(String name, int lightPin, int blindsPin, int airEnable1Pin, int airEnable2Pin, int airSpeedPin, int temperaturePin) {
    /**
     * @brief Constructor for the Room class when has light, blinds and airConditioner.
     *
     * @param name The name of the room.
     * @param lightPin The pin number for the light control.
     * @param blindsPin The pin number for the blinds control.
     * @param airEnablePin The pin number for the air conditioner enable control.
     * @param airSpeedPin The pin number for the air conditioner speed control.
     */

    _name = name;
    _devices["Lights"] = true;
    _devices["Blinds"] = true;
    _devices["Air"] = true;
    _devices["TemperatureSensor"] = true;
    _lightPin = lightPin;
    _blindsPin = blindsPin;
    _airEnable1Pin = airEnable1Pin;
    _airEnable2Pin = airEnable2Pin;
    _airSpeedPin = airSpeedPin;
    _temperaturePin = temperaturePin;
    _dht = new DHT(_temperaturePin, DHT11);

    initializeLight();
    initializeBlinds();
    initializeAir();
    initializeTemperatureSensor();
}

Room::Room(String name, int irrigationPin)
{
  /**
   * @brief Constructor for the Room class when has irrigation.
   *
   * @param name The name of the room.
   * @param irrigationPin The pin number for the irrigation control.
   */
  _name = name;
  _devices["Irrigation"] = true;
  _irrigationPin = irrigationPin;
  _dht = nullptr;
  initializeIrrigation();
}

// Getters
String Room::getName() {
    return _name;
}

String Room::getLightStatus() {
    return _lightStatus;
}

String Room::getBlindsStatus() {
    return _blindsStatus;
}

String Room::getAirStatus() {
    return _airStatus;
}

String Room::getAirSpeedStatus() {
    return _airSpeedStatus;
}

String Room::getIrrigationStatus() {
    return _irrigationStatus;
}

String Room::getIrrigationStartTime() {
    int hour = std::get<0>(_irrigationStartTime);
    int minute = std::get<1>(_irrigationStartTime);
    if (hour < 10) {
        if (minute < 10) {
            return "0" + String(hour) + ":0" + String(minute);
        }
        return "0" + String(hour) + ":" + String(minute);
    }
    return String(hour) + ":" + String(minute);
}

String Room::getIrrigationEndTime() {
    int hour = std::get<0>(_irrigationEndTime);
    int minute = std::get<1>(_irrigationEndTime);
    if (hour < 10) {
        if (minute < 10) {
            return "0" + String(hour) + ":0" + String(minute);
        }
        return "0" + String(hour) + ":" + String(minute);
    }
    return String(hour) + ":" + String(minute);
}

void Room::initializeTemperatureSensor() {
    _dht->begin();
}

float Room::getTemperature() {
    float temperature = _dht->readTemperature();
    if (isnan(temperature)) {
        return -999;
    }
    return temperature;
}

float Room::getHumidity() {
    float humidity = _dht->readHumidity();
    if (isnan(humidity)) {
        return -999;
    }
    return humidity;
}

bool Room::hasDevice(String deviceName) {
    return _devices[deviceName];
}

void Room::initializeLight() {
    pinMode(_lightPin, OUTPUT); 
    _lightStatus = "off";   
    setLightStatus(_lightStatus); 
}

void Room::setLightStatus(String status) {
    if (!hasDevice("Lights")) return;
    _lightStatus = status;
    if (status == "on") digitalWrite(_lightPin, HIGH);
    else if (status == "off") digitalWrite(_lightPin, LOW);
}

void Room::initializeBlinds() {
    _blindsServo.attach(_blindsPin, 500, 2500);
    _blindsStatus = "down";
    setBlindsStatus(_blindsStatus);
}

void Room::setBlindsStatus(String status) {
    if (!hasDevice("Blinds")) return;
    _blindsStatus = status;
    if (status == "up") _blindsServo.write(179);
    else if (status == "down") _blindsServo.write(0);
}

void Room::initializeAir() {
    pinMode(_airEnable1Pin, OUTPUT);
    pinMode(_airEnable2Pin, OUTPUT);
    pinMode(_airSpeedPin, OUTPUT);
    _airStatus = "off";
    _airSpeedStatus = "baja";
    setAirStatus(_airStatus);
    setAirSpeed(_airSpeedStatus);
}

void Room::setAirStatus(String status) {
    if (!hasDevice("Air")) return;
    _airStatus = status;
    if (status == "on") {
        digitalWrite(_airEnable1Pin, HIGH);
        digitalWrite(_airEnable2Pin, LOW);
    }
    else if (status == "off")
        digitalWrite(_airEnable1Pin, LOW);
        digitalWrite(_airEnable2Pin, LOW);
}

void Room::setAirSpeed(String speed) {
    if (!hasDevice("Air")) return; 
    _airSpeedStatus = speed;
    if (speed == "baja") _airSpeed = 85;
    else if (speed == "media") _airSpeed = 170;
    else if (speed == "alta") _airSpeed = 255;
    analogWrite(_airSpeedPin, _airSpeed);
}

void Room::initializeIrrigation() {
    pinMode(_irrigationPin, OUTPUT);
    _irrigationStatus = "off";
    setIrrigationStatus(_irrigationStatus);
}

void Room::setIrrigationStatus(String status) {
    if (!hasDevice("Irrigation")) return;
    _irrigationStatus = status;
    if (status == "on") _irrigationEnabled = true;
    else if (status == "off") _irrigationEnabled = false;
}

void Room::setIrrigationStartTime(int hour, int minute) {
    if (!hasDevice("Irrigation")) return;
    _irrigationStartTime = std::make_tuple(hour, minute);
}

void Room::setIrrigationEndTime(int hour, int minute) {
    if (!hasDevice("Irrigation")) return;
    _irrigationEndTime = std::make_tuple(hour, minute);
}

void Room::irrigate(int currentHour, int currentMinute) {
    if (_irrigationEnabled) {
        int startHour = std::get<0>(_irrigationStartTime);
        int startMinute = std::get<1>(_irrigationStartTime);
        int endHour = std::get<0>(_irrigationEndTime);
        int endMinute = std::get<1>(_irrigationEndTime);
        
        bool isWithinTimeRange = (currentHour > startHour || (currentHour == startHour && currentMinute >= startMinute)) &&
                (currentHour < endHour || (currentHour == endHour && currentMinute < endMinute));

        if (endHour > startHour || (endHour == startHour && endMinute > startMinute)) {
            digitalWrite(_irrigationPin, isWithinTimeRange ? HIGH : LOW);
        }

        else if (endHour < startHour || (endHour == startHour && endMinute < startMinute)) {   
            digitalWrite(_irrigationPin, isWithinTimeRange ? LOW : HIGH);
        }
        else if (endHour == startHour && endMinute == startMinute) {
            digitalWrite(_irrigationPin, LOW);
        }
    }
    else {
        digitalWrite(_irrigationPin, LOW);
    }
}