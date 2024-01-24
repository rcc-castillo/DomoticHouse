#include "RoomController.h"
#include "Irrigation.h"

RoomController::RoomController() {}

String RoomController::getDeviceData(String &source, const String &roomName, const String &deviceName) {
    DynamicJsonDocument jsonDoc(800);
    String jsonStr = source;
    DeserializationError error = deserializeJson(jsonDoc, jsonStr);
    JsonObject data = jsonDoc.as<JsonObject>();
    return data[roomName][deviceName].as<String>();
}

String RoomController::getRooms() {
    DynamicJsonDocument roomsJson(800);
    for (auto &roomPair : _roomMap) {
        Room &room = roomPair.second;
        JsonObject roomObject = roomsJson.createNestedObject(room.getName());

        if (room.hasDevice("Lights")) {
            roomObject.createNestedObject("lights")["state"] = room.getDeviceData("Lights", "State");
        }
        if (room.hasDevice("Blinds")) {
            roomObject.createNestedObject("blinds")["state"] = room.getDeviceData("Blinds", "State");
        }
        if (room.hasDevice("Air")) {
            JsonObject airObject = roomObject.createNestedObject("air");
            airObject["state"] = room.getDeviceData("Air", "State");
            airObject["speed"] = room.getDeviceData("Air", "Speed");
        }
        if (room.hasDevice("Irrigation")) {
            JsonObject irrigationObject = roomObject.createNestedObject("irrigation");
            irrigationObject["state"] = room.getDeviceData("Irrigation", "State");
            Serial.println(room.getDeviceData("Irrigation", "StartTime"));
            irrigationObject["startTime"] = room.getDeviceData("Irrigation", "StartTime");
            irrigationObject["endTime"] = room.getDeviceData("Irrigation", "EndTime");
        }
        if (room.hasDevice("DHT11Sensor")) {
            JsonObject temperatureObject = roomObject.createNestedObject("humidtemp");
            temperatureObject["temperature"] = room.getDeviceData("DHT11Sensor", "Temperature");
            temperatureObject["humidity"] = room.getDeviceData("DHT11Sensor", "Humidity");
        }
    }
    String jsonResponse;
    serializeJson(roomsJson, jsonResponse);
    return jsonResponse;
}

String RoomController::getHumidityAndTemperature() {
    StaticJsonDocument<200> jsonDocument;
    for (auto &roomPair : _roomMap) {
        Room &room = roomPair.second;
        if (!room.hasDevice("DHT11Sensor")) continue;
        JsonObject nestedObject = jsonDocument.createNestedObject(room.getName());
        nestedObject["temperature"] = room.getDeviceData("DHT11Sensor", "Temperature");
        nestedObject["humidity"] = room.getDeviceData("DHT11Sensor", "Humidity");
    }
    String jsonResponse;
    serializeJson(jsonDocument, jsonResponse);
    return jsonResponse;
}

String RoomController::handleDevice(String &source, const String &roomName, const String &deviceName, const String &deviceElement) {
    Room &room = _roomMap[roomName];
    String data = getDeviceData(source, roomName, deviceName);
    room.setDeviceState(deviceName, deviceElement, data);
    return deviceName + " " + deviceElement + " " + data;
}

void RoomController::addRoom(const String &roomName, const Room &room) {
    _roomMap[roomName] = room;
}

void RoomController::handleProgrammedCommand(const String &command, int currentHour, int currentMinute) {
    // Se podrian agregar mas comandos para otros dispositivos
    String device = "";
    if (command.equals("Irrigate")) device = "Irrigation";
    else return;
    for (auto &roomPair : _roomMap) {
        Room &room = roomPair.second;
        if (!room.hasDevice(device)) continue;
        room.getDevice(device)->handleProgrammedCommand(command, currentHour, currentMinute);
    }
}