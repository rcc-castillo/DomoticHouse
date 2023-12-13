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
    _hasLight = true;
    _hasBlinds = true;
    _hasAir = true;
    _hasTemperatureSensor = true;
    _lightPin = lightPin;
    _blindsPin = blindsPin;
    _airEnable1Pin = airEnable1Pin;
    _airEnable2Pin = airEnable2Pin;
    _airSpeedPin = airSpeedPin;
    _airSpeed = 105;
    _temperaturePin = temperaturePin;
    _dht = new DHT(_temperaturePin, DHT11);

    initializeLight();
    initializeBlinds();
    initializeAir();
}

Room::Room(String name, int irrigationPin) {
    /**
     * @brief Constructor for the Room class when has irrigation.
     *
     * @param name The name of the room.
     * @param irrigationPin The pin number for the irrigation control.
     */
    _name = name;
    _hasIrrigation = true;
    _irrigationPin = irrigationPin;
    _irrigationStatus = false;
    _dht = nullptr;
    initializeIrrigation();
}

String Room::getName() {
    return _name;
}

// Flags para saber si el cuarto tiene ciertos dispositivos
bool Room::hasLight() {
    return _hasLight;
}

bool Room::hasBlinds() {
    return _hasBlinds;
}

bool Room::hasAir() {
    return _hasAir;
}

bool Room::hasIrrigation() {
    return _hasIrrigation;
}

bool Room::hasTemperatureSensor() {
    return _hasTemperatureSensor;
}

void Room::initializeLight() {
    pinMode(_lightPin, OUTPUT);    // Configurar el pin del LED como salida
    digitalWrite(_lightPin, LOW); // Apagar el LED al inicio
}

void Room::setLightStatus(String status) {
    if (!hasLight()) return;
    if (status == "on") digitalWrite(_lightPin, HIGH);
    else if (status == "off") digitalWrite(_lightPin, LOW);
}

void Room::initializeBlinds() {
    _blindsServo.attach(_blindsPin, 500, 2500);
    _blindsServo.write(0);
}

void Room::setBlindsStatus(String status) {
    if (!hasBlinds()) return;
    if (status == "up") {
        _blindsServo.write(179);

    }
    else if (status == "down") _blindsServo.write(0);
}

void Room::initializeAir() {
    pinMode(_airEnable1Pin, OUTPUT);
    pinMode(_airEnable2Pin, OUTPUT);
    pinMode(_airSpeedPin, OUTPUT);
    analogWrite(_airSpeedPin, _airSpeed);
    setAirStatus("off");
}

void Room::setAirStatus(String status) {
    if (!hasAir()) return;
    if (status == "on") {
        digitalWrite(_airEnable1Pin, HIGH);
        digitalWrite(_airEnable2Pin, LOW);
    }
    else if (status == "off") 
        digitalWrite(_airEnable1Pin, LOW);
        digitalWrite(_airEnable2Pin, LOW);
}

void Room::setAirSpeed(String speed) {
    if (!hasAir()) return;
    if (speed == "baja") _airSpeed = 105;
    else if (speed == "media") _airSpeed = 170;
    else if (speed == "alta") _airSpeed = 255;
    analogWrite(_airSpeedPin, _airSpeed);
}

void Room::initializeIrrigation() {
    pinMode(_irrigationPin, OUTPUT);
    digitalWrite(_irrigationPin, LOW);
}

void Room::setIrrigationStatus(String status) {
    if (!hasIrrigation()) return;
    if (status == "on") _irrigationStatus = true;
    else if (status == "off") _irrigationStatus = false;
}

void Room::setIrrigationStartTime(int hour, int minute) {
    if (!hasIrrigation()) return;
    _irrigationStartTime = std::make_tuple(hour, minute);
}

void Room::setIrrigationEndTime(int hour, int minute) {
    if (!hasIrrigation()) return;
    _irrigationEndTime = std::make_tuple(hour, minute);
}

void Room::irrigate(int currentHour, int currentMinute) {
    if (!hasIrrigation()) return;
    if (_irrigationStatus) {
        int startHour = std::get<0>(_irrigationStartTime);
        int startMinute = std::get<1>(_irrigationStartTime);
        int endHour = std::get<0>(_irrigationEndTime);
        int endMinute = std::get<1>(_irrigationEndTime);
        
        bool isWithinTimeRange = (currentHour > startHour || (currentHour == startHour && currentMinute >= startMinute)) &&
                (currentHour < endHour || (currentHour == endHour && currentMinute < endMinute));

        // TODO: Test todas las posibilidades
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

// TODO: Comprobar si funciona el sensor de temperatura
void Room::initializeTemperatureSensor() {
    _dht->begin();
}

float Room::getTemperature() {
    float t = _dht->readTemperature();
    // Comprueba si la lectura ha fallado y, en caso afirmativo, devuelve un valor de error
    if (isnan(t)) {
        return -999;
    }
    return t;
}

float Room::getHumidity() {
    float h = _dht->readHumidity();
    // Comprueba si la lectura ha fallado y, en caso afirmativo, devuelve un valor de error
    if (isnan(h)) {
        return -999;
    }
    return h;
}
