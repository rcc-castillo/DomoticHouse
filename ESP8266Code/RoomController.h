#ifndef RoomController_h
#define RoomController_h

#include <map>
#include <ArduinoJson.h>
#include "Room.h"

class RoomController {
    private:
        std::map<String, Room> _roomMap;

    public:
        RoomController();
        String getDeviceData(String &source, const String &roomName, const String &deviceName);
        String getRooms();
        String getHumidityAndTemperature();
        String handleDevice(String &source, const String &roomName, const String &deviceName, const String &deviceElement);
        void addRoom(const String &roomName, const Room &room);
        void handleProgrammedCommand(const String &command, int currentHour, int currentMinute);

};

#endif