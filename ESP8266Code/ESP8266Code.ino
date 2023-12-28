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

std::map<String, Room> roomMap;

void setupRooms() {
    // Configura los datos para el salon
    roomMap["livingRoom"] = Room("livingRoom", 16, 12, 5, 4, 0, 13);
    roomMap["garden"] = Room("garden", 14);
}

void setupWifi() {
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

    String state = data[roomName][roomElement].as<String>();
    String text = "";

    if (roomElement == "lights") {
        room.setLightStatus(state);
        text = "Luces " + state;
    }
    else if (roomElement == "blinds") {
        room.setBlindsStatus(state);
        text = "Persianas " + state;
    }
    else if (roomElement == "air") {
        room.setAirStatus(state);
        text = "Aire acondicionado " + state;
    }
    else if (roomElement == "airSpeed") {
        room.setAirSpeed(state);
        text = "Velocidad del aire acondicionado " + state;
    }
    else if (roomElement == "irrigation") {
        room.setIrrigationStatus(state);
        text = "Riego " + state;
    }
    else if (roomElement == "irrigationStartTime") {
        int delimiterPos = state.indexOf(':');
        int hours = state.substring(0, delimiterPos).toInt();
        int minutes = state.substring(delimiterPos + 1).toInt();
        room.setIrrigationStartTime(hours, minutes);
        text = "Hora de inicio de riego " + state;
    }
    else if (roomElement == "irrigationEndTime") {
        int delimiterPos = state.indexOf(':');
        int hours = state.substring(0, delimiterPos).toInt();
        int minutes = state.substring(delimiterPos + 1).toInt();
        room.setIrrigationEndTime(hours, minutes);
        text = "Hora de fin de riego " + state;
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
            roomObject.createNestedObject("lights")["state"] = room.getLightStatus();
        }
        if (room.hasBlinds()) {
            roomObject.createNestedObject("blinds")["state"] = room.getBlindsStatus();
        }
        if (room.hasAir()) {
            JsonObject airObject = roomObject.createNestedObject("air");
            airObject["state"] = room.getAirStatus();
            airObject["speed"] = room.getAirSpeedStatus();
        }
        if (room.hasIrrigation()) {
            JsonObject irrigationObject = roomObject.createNestedObject("irrigation");
            irrigationObject["state"] = room.getIrrigationStatus();
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
        JsonObject nestedObject = jsonDocument.createNestedObject(room.getName());
        nestedObject["temperature"] = room.getTemperature();
        nestedObject["humidity"] = room.getHumidity();
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