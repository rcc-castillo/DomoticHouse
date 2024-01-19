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

    server.on("/sendLights", []() 
        { handleLights(server.arg("plain"), server.arg("roomName")); });

    server.on("/sendBlinds", []() 
        { handleBlinds(server.arg("plain"), server.arg("roomName")); });

    server.on("/sendAir", []() 
        { handleAir(server.arg("plain"), server.arg("roomName"), server.arg("element")); });

    server.on("/sendIrrigation", []() 
        { handleAir(server.arg("plain"), server.arg("roomName"), server.arg("element")); });

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

void handleSerial() {
    String data = Serial.readStringUntil('\n');
    Serial.println(data);
    if (data == "getRooms"){
        Serial.println(getRooms());
        return;
    }
    
    if (data == "getData") {
        Serial.println(getHumidityAndTemperature());
        return;
    }

    String roomName = data.substring(0, data.indexOf(','));
    data.remove(0, data.indexOf(',') + 1);

    String element = data.substring(0, data.indexOf(','));
    data.remove(0, data.indexOf(',') + 1);

    const String json = data;
    if (element == "Lights") {
        handleLights(json, roomName);
    }
    else if (element == "Blinds") {
        handleBlinds(json, roomName);
    }
    else if (element.startsWith("Air")) {
        handleAir(json, roomName, element);
    }
    else if (element.startsWith("Irrigation")) {
        handleIrrigation(json, roomName, element);
    }
}

JsonObject getData(const String &source) {
    JsonObject data;
    if (readJsonFromSource(source, data)) {
        return data;
    }
    else {
        return JsonObject();
    }
}

void handleLights(const String &source, String roomName) {
    Room &room = roomMap[roomName];
    JsonObject data = getData(source);
    if (data.isNull()) {
        server.send(400, "text/plain", "Error al analizar JSON");
        return;
    }
    String state = data[roomName]["Lights"].as<String>();
    room.setLightStatus(state);
    String text = "Luces " + state;
    server.send(200, "text/plain", roomName + ": " + text);
}

void handleBlinds(const String &source, String roomName) {
    Room &room = roomMap[roomName];
    JsonObject data = getData(source);
    if (data.isNull()) {
        server.send(400, "text/plain", "Error al analizar JSON");
        return;
    }
    String state = data[roomName]["Blinds"].as<String>();
    room.setBlindsStatus(state);
    String text = "Persianas " + state;
    server.send(200, "text/plain", roomName + ": " + text);
}

void handleAir(const String &source, String roomName, String element) {
    Room &room = roomMap[roomName];
    JsonObject data = getData(source);
    if (data.isNull()) {
        server.send(400, "text/plain", "Error al analizar JSON");
        return;
    }
    String state = data[roomName][element].as<String>();
    String text = "";
    if (element == "Air") {
        room.setAirStatus(state);
        text = "Aire acondicionado " + state;
    }
    else if (element == "AirSpeed") {
        room.setAirSpeed(state);
        text = "Velocidad del aire acondicionado " + state;
    }
    server.send(200, "text/plain", roomName + ": " + text);
}

void handleIrrigation(const String &source, String roomName, String element) {
    Room &room = roomMap[roomName];
    JsonObject data = getData(source);
    if (data.isNull()) {
        server.send(400, "text/plain", "Error al analizar JSON");
        return;
    }
    String state = data[roomName][element].as<String>();
    String text = "";
    if (element == "Irrigation") {
        room.setIrrigationStatus(state);
        text = "Riego " + state;
    }
    else if (element == "IrrigationStartTime") {
        int delimiterPos = state.indexOf(':');
        int hours = state.substring(0, delimiterPos).toInt();
        int minutes = state.substring(delimiterPos + 1).toInt();
        room.setIrrigationStartTime(hours, minutes);
        text = "Hora de inicio de riego " + state;
    }
    else if (element == "IrrigationEndTime") {
        int delimiterPos = state.indexOf(':');
        int hours = state.substring(0, delimiterPos).toInt();
        int minutes = state.substring(delimiterPos + 1).toInt();
        room.setIrrigationEndTime(hours, minutes);
        text = "Hora de fin de riego " + state;
    }
    server.send(200, "text/plain", roomName + ": " + text);
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
            JsonObject temperatureObject = roomObject.createNestedObject("humidtemp");
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

void loop() { 
    // Actualiza la hora
    timeClient.update();

    // Recorre el roomMap obteniendo la referencia al par <key, value>, Second se refiere al value
    for (auto &roomPair : roomMap) {
        Room &room = roomPair.second;
        if (room.hasIrrigation()) room.irrigate(timeClient.getHours(), timeClient.getMinutes());
    }

    // Leer datos desde el puerto serie
    if (Serial.available() > 0) {
        handleSerial();
    }
    // No hay datos en el puerto serie, intenta desde el servidor web
    else server.handleClient();
}