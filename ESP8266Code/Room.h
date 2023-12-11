#ifndef Room_h
#define Room_h

#include <Arduino.h>
#include <Servo.h>

class Room {
private:
    String _name;

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

    void initializeLight();
    void initializeBlinds();
    void initializeAir();
    void initializeIrrigation();

public:
    Room();
    Room(String name, int lightPin, int blindsPin, int airEnablePin, int airSpeedPin);
    Room(String name, int irrigationPin);
    String getName();
    void setLightStatus(String status);
    void setBlindsStatus(String status);
    void setAirStatus(String speed);
    void setAirSpeed(String speed);
    void setIrrigationStatus(String status);
    void setIrrigationStartTime(int hour, int minute);
    void setIrrigationEndTime(int hour, int minute);
    void irrigate();
};

#endif
