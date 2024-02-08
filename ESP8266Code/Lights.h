#ifndef Lights_h
#define Lights_h

#include <Arduino.h>
#include "Device.h"

class Lights : public Device {
    private:
        String _lightsState;
        void init() override;

    public:
        Lights(int pin, const String &name);
        String get(const String &deviceElement) override;
        void set(const String &deviceElement, const String &data) override;
        void handleProgrammedCommand(const String &command, int currentHour, int currentMinute) override;
};

#endif