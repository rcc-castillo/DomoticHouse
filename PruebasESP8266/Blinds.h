#ifndef Blinds_h
#define Blinds_h

#include <Arduino.h>
#include "Device.h"
#include <Servo.h>

class Blinds : public Device{
    private:
        String _blindsState;
        Servo _blindsServo;
        void init() override;
    
    public:
        Blinds(int pin, const String &name);
        String get(const String &deviceElement) override;
        void set(const String &deviceElement, const String &data) override;
        void handleProgrammedCommand(const String &command, int currentHour, int currentMinute) override;
};
#endif