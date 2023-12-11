#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <map>
#include "Room.h"
#include "ReadJson.h"
#include "WifiCredentials.h"

ESP8266WebServer server(80);
IPAddress local_IP(192, 168, 118, 249);
// Set your Gateway IP address
IPAddress gateway(192, 168, 118, 1);

IPAddress subnet(255, 255, 0, 0);

std::map<String, Room> roomMap;

void setupRooms() {
    // Configura los datos para el salon
    roomMap["livingroom"] = Room("livingRoom", LED_BUILTIN, 14, 13, 12);
    roomMap["garden"] = Room("garden", LED_BUILTIN, 4, 0, 2);
}

void setupWifi() {
    // Configures static IP address 
    if (!WiFi.config(local_IP, gateway, subnet))
        Serial.println("STA Failed to configure");

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
    server.on("/livingroom", []() {
        String source = server.arg("plain");
        handleRoom(source); 
    });
    server.on("/data", sendData);
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
    Serial.println(text);
    
    server.send(200, "text/plain", roomName + ": " + text);
}

void handleRoom(String &source) {
    JsonObject data;
    Serial.println("llegamos aqui");
    if (readJsonFromSource(source, data)) {
        String roomName = data.begin()->key().c_str();
        if (roomMap.count(roomName) == 0) {
            Serial.println("Room not found: " + roomName);
            return;
    }
        handleRoomData(data, roomName);
    }
    else {
        server.send(400, "text/plain", "Error al analizar JSON");
    }
}

void sendData(){
    StaticJsonDocument<200> jsonDocument;
    jsonDocument["temperature"] = 25.4;
    jsonDocument["humidity"] = 60.2;
    String jsonResponse;
    serializeJson(jsonDocument, jsonResponse);
    server.send(200, "application/json", jsonResponse);

    // Si hay una conexión de puerto serie abierta, envía los datos por ahí también
    if (Serial) {
        Serial.println(jsonResponse);
    }
}
void loop() { 
    // TODO: LLamar a room.irrigate()
    // Leer datos desde el puerto serie
    if (Serial.available() > 0) {
        String source = Serial.readStringUntil('\n');
        handleRoom(source);
    }
    // No hay datos en el puerto serie, intenta desde el servidor web
    else {
        server.handleClient();
    }
}
