#ifndef AirConditioner_h
#define AirConditioner_h

#include <Arduino.h>
#include "Device.h"

class AirConditioner : public Device{
    private:
        int _enablePin1;
        int _enablePin2;
        int _speedPin;
        int _airSpeed;
        String _airState;
        String _airSpeedState;
        void init() override;
    
    public:
        AirConditioner(int enablePin1, int enablePin2, int speedPin, const String &name);
        String get(const String &deviceElement) override;
        void set(const String &deviceElement, const String &data) override;
        void setAirState(const String &data);
        void setAirSpeed(const String &data);
        void handleProgrammedCommand(const String &command, int currentHour, int currentMinute) override;
};
#endif