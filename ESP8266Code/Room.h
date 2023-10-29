#ifndef Room_h
#define Room_h

#include <Arduino.h>

struct LightData {
    bool status;
    int pin;
};

class Room {
private:
    String _name;
    LightData _light;
    void initializeLight();

public:
    Room();
    Room(String name, int lightPin);
    String getName();
    int getLightPin();
    void setLightStatus(uint8_t status);
};

#endif
