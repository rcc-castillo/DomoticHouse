#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <NTPClient.h>
#include <map>
#include "WifiCredentials.h"
#include "ESPServer.h"
#include "RoomController.h"
#include "Room.h"
#include "Device.h"
#include "Lights.h"
#include "Blinds.h"
#include "AirConditioner.h"
#include "Irrigation.h"
#include "DHTSensor.h"


WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "europe.pool.ntp.org", 3600, 5000);

RoomController roomController;
ESPServer server(roomController);

void setupRooms() {
    Device* lights = new Lights(16, "LivingRoomLights");
    Device* blinds = new Blinds(12, "LivingRoomBlinds");
    Device* airConditioner = new AirConditioner(5, 4, 0, "LivingRoomAirConditioner");
    Device* tempHumidSensor = new DHTSensor(13, "LivingRoomTempHumidSensor");
    std::map<String, Device*> livingRoomDevices = {
        {"Lights", lights},
        {"Blinds", blinds},
        {"Air", airConditioner},
        {"DHT11Sensor", tempHumidSensor}
    };

    Device* irrigation = new Irrigation(14, "GardenIrrigation");
    std::map<String, Device*> gardenDevices = {
        {"Irrigation", irrigation}
    };

    Room* livingRoom = new Room("livingRoom", livingRoomDevices);
    roomController.addRoom(livingRoom->getName(), *livingRoom);
    Room* garden = new Room("garden", gardenDevices);
    roomController.addRoom(garden->getName(), *garden);
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


void handleSerial() {
    String message = Serial.readStringUntil('\n');
    if (message.equals("getRooms")) {
        Serial.println(roomController.getRooms());
    }
    else if (message.equals("getData")) {
        Serial.println(roomController.getHumidityAndTemperature());
    }
    else {
        String roomName = message.substring(0, message.indexOf(','));
        message.remove(0, message.indexOf(',') + 1);
        String deviceName = message.substring(0, message.indexOf(','));
        message.remove(0, message.indexOf(',') + 1);
        String deviceElement = message.substring(0, message.indexOf(','));
        message.remove(0, message.indexOf(',') + 1);
        String source = message;
        Serial.println(roomController.handleDevice(source, roomName, deviceName, deviceElement));
    }
}

void setup() {
    Serial.begin(9600);
    setupWifi();
    setupRooms();
    server.setupServer();
    timeClient.begin();
}

void loop() { 
    // Actualiza la hora
    timeClient.update();

    // Riega en las habitaciones con sistema de irrigacion si es la hora
    roomController.handleProgrammedCommand("Irrigate", timeClient.getHours(), timeClient.getMinutes());

    // Leer datos desde el puerto serie
    if (Serial.available()) handleSerial();
    // No hay datos en el puerto serie, intenta desde el servidor web
    else server.handleClient();
}