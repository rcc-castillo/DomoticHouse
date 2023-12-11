#include "Room.h"

Room::Room(String name, int lightPin, int blindsPin, int airEnablePin, int airSpeedPin, int temperaturePin) {
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
    _airEnablePin = airEnablePin;
    _airSpeedPin = airSpeedPin;
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
    digitalWrite(_lightPin, HIGH); // Apagar el LED al inicio
}

void Room::setLightStatus(String status) {
    if (!hasLight()) return;
    if (status == "on") digitalWrite(_lightPin, LOW);
    else if (status == "off") digitalWrite(_lightPin, HIGH);
}

void Room::initializeBlinds() {
    _blindsServo.attach(_blindsPin);
    _blindsServo.write(0);
}

void Room::setBlindsStatus(String status) {
    if (!hasBlinds()) return;
    if (status == "up") _blindsServo.write(180);
    else if (status == "down") _blindsServo.write(0);
}

void Room::initializeAir() {
    pinMode(_airEnablePin, OUTPUT);
    pinMode(_airSpeedPin, OUTPUT);
    setAirStatus("off");
}

void Room::setAirStatus(String status) {
    if (!hasAir()) return;
    if (status == "on") digitalWrite(_airEnablePin, LOW);
    else if (status == "off") digitalWrite(_airEnablePin, HIGH);
}

void Room::setAirSpeed(String speed) {
    if (!hasAir()) return;
    if (speed == "baja") digitalWrite(_airSpeedPin, 85);
    else if (speed == "media") digitalWrite(_airSpeedPin, 170);
    else if (speed == "alta") digitalWrite(_airSpeedPin, 255);
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

void Room::irrigate() {
    if (!hasIrrigation()) return;
    if (_irrigationStatus)
    {
        int startHour = std::get<0>(_irrigationStartTime);
        int startMinute = std::get<1>(_irrigationStartTime);
        int endHour = std::get<0>(_irrigationEndTime);
        int endMinute = std::get<1>(_irrigationEndTime);

        time_t currentTime;
        struct tm *localTime;

        time(&currentTime);                  // Get the current time
        localTime = localtime(&currentTime); // Convert the current time to the local time

        int currentHour = localTime->tm_hour;
        int currentMin = localTime->tm_min;
        Serial.println(currentHour);
        Serial.println(currentMin);

        // The irrigation should be on from startHour to midnight and from midnight to endHour
        if (endHour < startHour || (endHour == startHour && endMinute < startMinute))
        {
            if ((currentHour > startHour || (currentHour == startHour && currentMin >= startMinute)) ||
                (currentHour < endHour || (currentHour == endHour && currentMin <= endMinute)))
            {
                digitalWrite(_irrigationPin, HIGH);
            }
            else
            {
                digitalWrite(_irrigationPin, LOW);
            }
        }

        // The irrigation should be on from startHour to endHour
        else
        {
            if (currentHour >= startHour && currentHour <= endHour && currentMin >= startMinute && currentMin <= endMinute)
            {
                digitalWrite(_irrigationPin, HIGH);
            }
            else
            {
                digitalWrite(_irrigationPin, LOW);
            }
        }
    }
    else
    {
        digitalWrite(_irrigationPin, LOW);
    }
}

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
