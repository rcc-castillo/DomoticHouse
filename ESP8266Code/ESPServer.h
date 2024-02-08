#ifndef Server_h
#define Server_h

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include "RoomController.h"

class ESPServer
{
private:
    ESP8266WebServer server;
    RoomController &roomController;

public:
    ESPServer(RoomController &roomController);
    void setupServer();
    void handleRequest(const String &path);
    void handleClient();
    void send(int statusCode, const String &message);
};

#endif