#include "Room.h"
#include <ctime>

Room::Room() {
}


Room::Room(String name, int lightPin, int blindsPin, int airEnablePin, int airSpeedPin) {
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
    _lightPin = lightPin;
    _blindsPin = blindsPin;
    _airEnablePin = airEnablePin;
    _airSpeedPin = airSpeedPin;
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
    _irrigationPin = irrigationPin;
    initializeIrrigation();
}

String Room::getName() {
    return _name;
}

void Room::initializeLight() {
    pinMode(_lightPin, OUTPUT);  // Configurar el pin del LED como salida
    digitalWrite(_lightPin, HIGH);  // Apagar el LED al inicio
}

void Room::setLightStatus(String status) {
    if (status == "on") {
        digitalWrite(_lightPin, LOW);
    }
    else if (status == "off")
    {
        digitalWrite(_lightPin, HIGH);
    }
}

void Room::initializeBlinds() {
    _blindsServo.attach(_blindsPin);  
    _blindsServo.write(0);
}

void Room::setBlindsStatus(String status) {
  if (status == "up") _blindsServo.write(180);
  else if (status == "down") _blindsServo.write(0);
}

void Room::initializeAir() {
  pinMode(_airEnablePin, OUTPUT);
  pinMode(_airSpeedPin, OUTPUT);
  setAirStatus("off");
}

void Room::setAirStatus(String status) {
    if (status == "on") digitalWrite(_airEnablePin, LOW);
    else if (status == "off") digitalWrite(_airEnablePin, HIGH);
}

void Room::setAirSpeed(String speed) {
    if (speed == "baja") digitalWrite(_airSpeedPin, 85);
    else if (speed == "media") digitalWrite(_airSpeedPin, 170);
    else if (speed == "alta") digitalWrite(_airSpeedPin, 255);
}

void Room::initializeIrrigation() {
    pinMode(_irrigationPin, OUTPUT);
    digitalWrite(_irrigationPin, LOW);
}

void Room::setIrrigationStatus(String status) {
    if (status == "on") _irrigationStatus = true;
    else if (status == "off") _irrigationStatus = false;
}

void Room::setIrrigationStartTime(int hour, int minute) {
    _irrigationStartTime = std::make_tuple(hour, minute);
}

void Room::setIrrigationEndTime(int hour, int minute) {
    _irrigationEndTime = std::make_tuple(hour, minute);
}

void Room::irrigate() {
    if (_irrigationStatus) {
        int startHour = std::get<0>(_irrigationStartTime);
        int startMinute = std::get<1>(_irrigationStartTime);
        int endHour = std::get<0>(_irrigationEndTime);
        int endMinute = std::get<1>(_irrigationEndTime);
        
        
        time_t currentTime;
        struct tm *localTime;

        time( &currentTime );                   // Get the current time
        localTime = localtime( &currentTime );  // Convert the current time to the local time

        int currentHour   = localTime->tm_hour;
        int currentMin    = localTime->tm_min;
        Serial.println(currentHour);
        Serial.println(currentMin);

        // The irrigation should be on from startHour to midnight and from midnight to endHour
        if (endHour < startHour || (endHour == startHour && endMinute < startMinute)) {
            if ((currentHour > startHour || (currentHour == startHour && currentMin >= startMinute)) || 
                (currentHour < endHour || (currentHour == endHour && currentMin <= endMinute))) {
                digitalWrite(_irrigationPin, HIGH);
            }
            else {
                digitalWrite(_irrigationPin, LOW);
            }
        }
        
        // The irrigation should be on from startHour to endHour
        else {
            if (currentHour >= startHour && currentHour <= endHour && currentMin >= startMinute && currentMin <= endMinute) {
                digitalWrite(_irrigationPin, HIGH);
            }
            else {
                digitalWrite(_irrigationPin, LOW);
            }
        }
    }
    else {
        digitalWrite(_irrigationPin, LOW);
    }
}