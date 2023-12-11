#ifndef Room_h
#define Room_h

#include <Arduino.h>
#include <Servo.h>
#include "DHT.h"
#include <ctime>

class Room {
private:
    String _name;

    // Flags para saber si el cuarto tiene ciertos dispositivos
    bool _hasLight = false;
    bool _hasBlinds = false;
    bool _hasAir = false;
    bool _hasIrrigation = false;
    bool _hasTemperatureSensor = false;

    // Luces
    int _lightPin;

    // Persianas
    int _blindsPin;
    Servo _blindsServo;
    // Aire acondicionado
    int _airEnablePin; // Pin para controlar encendido y apagado del motor
    int _airSpeedPin;  // Pin para controlar la velocidad del motor

    // Riego
    int _irrigationPin;
    bool _irrigationStatus;
    std::tuple<int, int> _irrigationStartTime;
    std::tuple<int, int> _irrigationEndTime;

    // Temperatura
    int _temperaturePin;
    DHT* _dht;

    void initializeLight();
    void initializeBlinds();
    void initializeAir();
    void initializeIrrigation();
    void initializeTemperatureSensor();

public:
    Room(String name, int lightPin, int blindsPin, int airEnablePin, int airSpeedPin, int temperaturePin);
    Room(String name, int irrigationPin);
    String getName();
    
    bool hasLight();
    bool hasBlinds();
    bool hasAir();
    bool hasIrrigation();
    bool hasTemperatureSensor();

    void setLightStatus(String status);
    void setBlindsStatus(String status);
    void setAirStatus(String speed);
    void setAirSpeed(String speed);
    void setIrrigationStatus(String status);
    void setIrrigationStartTime(int hour, int minute);
    void setIrrigationEndTime(int hour, int minute);
    void irrigate();
    float getTemperature(); 
    float getHumidity();
};

#endif
