#ifndef Room_h
#define Room_h

#include <Arduino.h>
#include <Servo.h>

class Room {
private:
    String _name;
    int _lightPin;
    int _blindsPin;
    Servo _blindsServo;
    int _airEnablePin; // Pin para controlar encendido y apagado del motor
    int _airSpeedPin;  // Pin para controlar la velocidad del motor
    void initializeLight();
    void initializeBlinds();
    void initializeAir();

public:
    Room();
    Room(String name, int lightPin, int blindsPin, int airEnablePin, int airSpeedPin);
    String getName();
    void setLightStatus(String status);
    void setBlindsStatus(String status);
    void setAirStatus(String speed);
    void setAirSpeed(String speed);
};

#endif
