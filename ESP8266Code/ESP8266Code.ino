#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <WiFiUdp.h>
#include <NTPClient.h>
#include <map>
#include "Room.h"
#include "ReadJson.h"
#include "WifiCredentials.h"

ESP8266WebServer server(80);
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "europe.pool.ntp.org", 3600, 5000);


IPAddress local_IP(192, 168, 118, 249);
// Set your Gateway IP address
IPAddress gateway(192, 168, 118, 1);

IPAddress subnet(255, 255, 0, 0);

std::map<String, Room> roomMap;

void setupRooms() {
    // Configura los datos para el salon
    roomMap["livingRoom"] = Room("livingRoom", 16, 12, 5, 4, 0, 13);
    roomMap["garden"] = Room("garden", 14);
}

void setupWifi() {
    // Configures static IP address 
    // if (!WiFi.config(local_IP, gateway, subnet))
    //     Serial.println("STA Failed to configure");

    WiFi.begin(ssid, password);

    // Espera hasta que la conexión WiFi se establezca
    while (WiFi.status() != WL_CONNECTED) {
        Serial.println("...");
        delay(500);
    }

    // Muestra la dirección IP asignada
    Serial.println("Nodemcu(esp8266) is connected to the ssid :");
    Serial.println(WiFi.localIP());
}

void setupServer() {
    server.on("/", []()
        { server.send(200, "text/plain", "Conection established"); });
    server.onNotFound([]()
        { server.send(404, "text/plain", "404: Not found"); });
    server.on("/sendData", []() {
        String source = server.arg("plain");
        handleRoom(source);
    });
    server.on("/getData", []()
        { server.send(200, "text/plain", getHumidityAndTemperature()); });
    
    server.on("/getRooms", []()
        { server.send(200, "text/plain", getRooms()); });
    server.begin();
}

void setup() {
    // Inicializa la comunicación serial
    Serial.begin(9600);

    // Inicializa los cuartos
    setupRooms();

    // Inicializa la conexión WiFi
    setupWifi();

    // Inicializa el servidor web
    setupServer();

    // Inicializa el cliente NTP
    timeClient.begin();
}

void handleRoomData(JsonObject &data, String roomName) {
    Room &room = roomMap[roomName];
    String roomElement = data[roomName].as<JsonObject>().begin()->key().c_str();

    String status = data[roomName][roomElement].as<String>();
    String text = "";

    if (roomElement == "lights") {
        room.setLightStatus(status);
        text = "Luces " + status;
    }
    else if (roomElement == "blinds") {
        room.setBlindsStatus(status);
        text = "Persianas " + status;
    }
    else if (roomElement == "airState") {
        room.setAirStatus(status);
        text = "Aire acondicionado " + status;
    }
    else if (roomElement == "airSpeed") {
        room.setAirSpeed(status);
        text = "Velocidad del aire acondicionado " + status;
    }
    else if (roomElement == "irrigationState") {
        room.setIrrigationStatus(status);
        text = "Riego " + status;
    }
    else if (roomElement == "irrigationStartTime") {
        int delimiterPos = status.indexOf(':');
        int hours = status.substring(0, delimiterPos).toInt();
        int minutes = status.substring(delimiterPos + 1).toInt();
        room.setIrrigationStartTime(hours, minutes);
        text = "Hora de inicio de riego " + status;
    }
    else if (roomElement == "irrigationEndTime") {
        int delimiterPos = status.indexOf(':');
        int hours = status.substring(0, delimiterPos).toInt();
        int minutes = status.substring(delimiterPos + 1).toInt();
        room.setIrrigationEndTime(hours, minutes);
        text = "Hora de fin de riego " + status;
    }
    else {
        text = "Elemento no encontrado: " + roomElement;
        Serial.println(roomName + ": " + text);
        server.send(404, "text/plain", roomName + ": " + text);
        return;
    }

    if (Serial) Serial.println(text);
    server.send(200, "text/plain", roomName + ": " + text);
}

void handleRoom(String &source) {
    JsonObject data;
    if (readJsonFromSource(source, data)) {
        String roomName = data.begin()->key().c_str();
        if (roomMap.count(roomName) == 0) {
            Serial.println("Room not found: " + roomName);
            server.send(404, "text/plain", "Room not found: " + roomName);
            return;
        }
        handleRoomData(data, roomName);
    }
    else {
        server.send(400, "text/plain", "Error al analizar JSON");
    }
}

String getRooms() {
    DynamicJsonDocument roomsJson(800);
    for (auto &roomPair : roomMap) {
        Room &room = roomPair.second;
        JsonObject roomObject = roomsJson.createNestedObject(room.getName());

        if (room.hasLight()) {
            roomObject.createNestedObject("lights")["status"] = room.getLightStatus();
        }
        if (room.hasBlinds()) {
            roomObject["blinds"] = room.getBlindsStatus();
        }
        if (room.hasAir()) {
            JsonObject airObject = roomObject.createNestedObject("air");
            airObject["status"] = room.getAirStatus();
            airObject["speedStatus"] = room.getAirSpeedStatus();
        }
        if (room.hasIrrigation()) {
            JsonObject irrigationObject = roomObject.createNestedObject("irrigation");
            irrigationObject["status"] = room.getIrrigationStatus();
            irrigationObject["startTime"] = room.getIrrigationStartTime();
            irrigationObject["endTime"] = room.getIrrigationEndTime();
        }
        if (room.hasTemperatureSensor()) {
            JsonObject temperatureObject = roomObject.createNestedObject("humidTemp");
            temperatureObject["temperature"] = room.getTemperature();
            temperatureObject["humidity"] = room.getHumidity();
        }
    }
    String jsonResponse;
    serializeJson(roomsJson, jsonResponse);
    return jsonResponse;
}

String getHumidityAndTemperature() {
    StaticJsonDocument<200> jsonDocument;
    for (auto &roomPair : roomMap) {
        Room &room = roomPair.second;
        if (!room.hasTemperatureSensor()) continue;
        float temperature = room.getTemperature();
        float humidity = room.getHumidity();
        String roomName = room.getName();
        JsonObject nestedObject = jsonDocument.createNestedObject(roomName);
        nestedObject["temperature"] = temperature;
        nestedObject["humidity"] = humidity;
    }
    String jsonResponse;
    serializeJson(jsonDocument, jsonResponse);
    return jsonResponse;
}

void sendData() {
    if (Serial) Serial.println(getHumidityAndTemperature());
}

void loop() { 
    // Actualiza la hora
    timeClient.update();
    // Recorre el roomMap obteniendo la referencia al par <key, value>, Second se refiere al value
    for (auto &roomPair : roomMap) {
        Room &room = roomPair.second;
        room.irrigate(timeClient.getHours(), timeClient.getMinutes());
    }

    // Leer datos desde el puerto serie
    if (Serial.available() > 0) {
        String source = Serial.readStringUntil('\n');
        handleRoom(source);
    }
    // No hay datos en el puerto serie, intenta desde el servidor web
    else {
        server.handleClient();
    }
    sendData();
}