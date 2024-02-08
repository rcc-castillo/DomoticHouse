#ifndef Room_h
#define Room_h

#include <Arduino.h>
#include "Device.h"
#include <map>

class Room {
    private:
        String _name;
        std::map<String, Device*> _devices;

    public:
        Room(){};
        Room(String name, std::map<String, Device*> devices);

        String getName();
        bool hasDevice(const String &deviceName);
        String getDeviceData(const String &deviceName, const String &deviceElement);
        void setDeviceState(const String &deviceName, const String &deviceElement, const String &state);
        Device* getDevice(const String &deviceName);
};

#endif
