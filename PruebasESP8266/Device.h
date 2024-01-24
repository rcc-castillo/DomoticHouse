#ifndef Device_h
#define Device_h

#include <Arduino.h>

class Device {
    protected:
        int _pin;
        String _name;

    public:
        Device(int pin, const String &name);
        virtual String get(const String& data) = 0;
        virtual void set(const String &deviceElement, const String &data) = 0;
        virtual void init() = 0;
        String getName() { return _name; };
        virtual void handleProgrammedCommand(const String &command, int currentHour, int currentMinute) = 0;
};

#endif 