#ifndef Room_h
#define Room_h

#include <Arduino.h>
#include <Servo.h>
#include "DHT.h"
#include <ctime>
#include <map>

class Room {
private:
    String _name;

    // Flags para saber si el cuarto tiene ciertos dispositivos
    std::map<String, bool> _devices = {
        {"Lights", false},
        {"Blinds", false},
        {"Air", false},
        {"Irrigation", false},
        {"TemperatureSensor", false}
    };

    // Luces
    int _lightPin;
    String _lightStatus;

    // Persianas
    int _blindsPin;
    Servo _blindsServo;
    String _blindsStatus;

    // Aire acondicionado
    int _airEnable1Pin; // Pin para controlar encendido y apagado del motor
    int _airEnable2Pin; // Pin para controlar encendido y apagado del motor
    int _airSpeedPin;  // Pin para controlar la velocidad del motor
    int _airSpeed;
    String _airStatus;
    String _airSpeedStatus;

    // Riego
    int _irrigationPin;
    bool _irrigationEnabled;
    String _irrigationStatus;
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
    Room();
    Room(String name, int lightPin, int blindsPin, int airEnable1Pin, int airEnable2Pin, int airSpeedPin, int temperaturePin);
    Room(String name, int irrigationPin);

    String getName();
    String getLightStatus();
    String getBlindsStatus();
    String getAirStatus();
    String getAirSpeedStatus();
    String getIrrigationStatus();
    String getIrrigationStartTime();
    String getIrrigationEndTime();
    float getTemperature(); 
    float getHumidity();

    bool hasDevice(String deviceName);

    void setLightStatus(String status);
    void setBlindsStatus(String status);
    void setAirStatus(String speed);
    void setAirSpeed(String speed);
    void setIrrigationStatus(String status);
    void setIrrigationStartTime(int hour, int minute);
    void setIrrigationEndTime(int hour, int minute);
    void irrigate(int hour, int minute);
};

#endif
