#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <map>
#include "Room.h"

ESP8266WebServer server(80);
IPAddress local_IP(192, 168, 208, 249);
// Set your Gateway IP address
IPAddress gateway(192, 168, 208, 1);

IPAddress subnet(255, 255, 0, 0);

// WiFi connection credentials
const char *ssid = "Rodrigo's Galaxy S21 FE 5G";
const char *password = "telesala";

std::map<String, Room> roomMap;

void setup()
{
    // Configura los datos para el salon
    Room livingRoom = Room("living", LED_BUILTIN, 14, 13, 12);
    roomMap["living"] = livingRoom;

    // Inicializa la comunicación serial
    Serial.begin(9600);

    // Conexión WiFi

    // Configures static IP address
    /**/
    if (!WiFi.config(local_IP, gateway, subnet)) 
        Serial.println("STA Failed to configure");

    WiFi.begin(ssid, password);

    // Espera hasta que la conexión WiFi se establezca
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.println("...");
        delay(500);
    }

    // Muestra la dirección IP asignada
    Serial.println("Nodemcu(esp8266) is connected to the ssid :");
    Serial.println(WiFi.localIP());

    // Inicializa el servidor
    server.on("/", []()
            { server.send(200, "text/plain", "Conection established"); });
    server.onNotFound([]()
            { server.send(404, "text/plain", "404: Not found"); });
    server.on("/room", handleData);
    server.begin();
}

bool readJsonFromSource(String &source, JsonObject &data)
{
    // Create a JSON buffer and parse the data into it
    const size_t bufferSize = 600;
    StaticJsonDocument<bufferSize> jsonDoc;
    char jsonStr[bufferSize];

    source.toCharArray(jsonStr, bufferSize);

    DeserializationError error = deserializeJson(jsonDoc, jsonStr);

    // Verify there is no error parsing JSON
    if (!error)
    {
        data = jsonDoc.as<JsonObject>();
        return true;
    }
    else
    {
        Serial.print("Error al analizar JSON: ");
        Serial.println(error.c_str());
        return false;
    }
}

void handleData()
{
    // Leer datos desde el puerto serie
    JsonObject data;
    String source = server.arg("plain");
    handleRoom(source);
}

void handleRoom(String &source) {
    JsonObject data;
    if (readJsonFromSource(source, data)) {
        String roomName = data.begin()->key().c_str();
        Room room = roomMap[roomName];
        String roomElement = data[roomName].as<JsonObject>().begin()->key().c_str();

        Serial.println("Room: " + roomName + " | Elemento: " + roomElement);
        String text = "";
        if (roomElement == "lights") {
            String status = data[roomName][roomElement].as<String>();
            room.setLightStatus(status);
            text = "Luces " + status;
        }
        else if (roomElement == "blinds") {
            String status = data[roomName][roomElement].as<String>();
            room.setBlindsStatus(status);
            text = "Persianas " + status;
        }
        else if (roomElement == "airState") {
            String status = data[roomName][roomElement].as<String>();
            room.setAirStatus(status);
            text = "Aire acondicionado " + status;
            
        }
        else if (roomElement == "airSpeed") {
            String speed = data[roomName][roomElement].as<String>();
            room.setAirSpeed(speed);
            text = "Velocidad del aire acondicionado " + speed;
        }
        Serial.println(text);
        
        server.send(200, "text/plain", text);
    }
    else {
        server.send(400, "text/plain", "Error al analizar JSON");
    }
}

void loop()
{   
    if (Serial.available() > 0)
    {
        // Leer datos desde el puerto serie
        JsonObject data;
        String source = Serial.readStringUntil('\n');
        handleRoom(source);
    }
    else
    {
        // No hay datos en el puerto serie, intenta desde el servidor web
        server.handleClient();
    }
}
