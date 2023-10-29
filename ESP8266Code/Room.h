#ifndef Room_h
#define Room_h

#include <Arduino.h>

class Room {
private:
    String _name;
    int _lightPin;
    void initializeLight();

public:
    Room();
    Room(String name, int lightPin);
    String getName();
    int getLightPin();
    void setLightStatus(uint8_t status);
};

#endif
