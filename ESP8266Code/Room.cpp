#include "Room.h"

Room::Room(String name, std::map<String, Device*> devices) {
    _name = name;
    _devices = devices;   
}

String Room::getName() {
    return _name;
}

bool Room::hasDevice(const String &deviceName) {
    return _devices.find(deviceName) != _devices.end();
}

String Room::getDeviceData(const String &deviceName, const String &deviceElement) {
    if (!hasDevice(deviceName)) return"La habitación no tiene ese" + deviceName;
    return _devices[deviceName]->get(deviceElement);
}

void Room::setDeviceState(const String &deviceName, const String &deviceElement, const String &data) {
    if (!hasDevice(deviceName)) return;
    return _devices[deviceName]->set(deviceElement, data);
}

Device* Room::getDevice(const String &deviceName) {
    if (!hasDevice(deviceName)) return nullptr;
    return _devices[deviceName];
}
