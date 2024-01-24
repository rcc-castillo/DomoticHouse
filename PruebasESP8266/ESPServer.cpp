#include "ESPServer.h"

ESPServer::ESPServer(RoomController& roomController) : roomController(roomController) {}

void ESPServer::setupServer() {
    server.on("/", [this]()
        { server.send(200, "text/plain", "Conection established"); });

    server.onNotFound([this]()
        { server.send(404, "text/plain", "404: Not found"); });

    server.on("/getData", [this]()
        { server.send(200, "text/plain", roomController.getHumidityAndTemperature()); });
    
    server.on("/getRooms", [this]()
        { server.send(200, "text/plain", roomController.getRooms()); });

    server.on("/sendLights", [this]()
        { handleRoom("/sendLights"); });

    server.on("/sendBlinds", [this]()
        { handleRoom("/sendBlinds"); });

    server.on("/sendAir", [this]()
        { handleRoom("/sendAir"); });

    server.on("/sendIrrigation", [this]()
        { handleRoom("/sendIrrigation"); });

    server.begin();
}

void ESPServer::handleRoom(const String &path) {
        String source = server.arg("plain");
        String roomName = server.arg("roomName");
        String deviceName = server.arg("deviceName");
        String deviceElement = server.arg("deviceElement");
        String text = roomController.handleDevice(source, roomName, deviceName, deviceElement);
        if (text.isEmpty()) server.send(400, "text/plain", "[ERROR] Error al analizar JSON");
        else server.send(200, "text/plain", roomName + ": " + text);
}

void ESPServer::handleClient() {
    server.handleClient();
}

void ESPServer::send(int statusCode, const String &message) {
    server.send(statusCode, "text/plain", message);
}