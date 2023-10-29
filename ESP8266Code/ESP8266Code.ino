#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <map>

ESP8266WebServer server(80);
IPAddress local_IP(192, 168, 52, 249);
// Set your Gateway IP address
IPAddress gateway(192, 168, 52, 1);

IPAddress subnet(255, 255, 0, 0);

// WiFi connection credentials
const char *ssid = "Rodrigo's Galaxy S21 FE 5G";
const char *password = "telesala";

// Define una estructura para los datos de temperatura y humedad
struct TempHumidData
{
    float temperature;
    float humidity;
    int pin;
};

// Define una estructura para los datos de la habitación
struct RoomData
{
    TempHumidData tempHumid;
    int lightPin;
    int blindsPin;
    int airPin;
};

std::map<String, RoomData> roomMap;

void setup()
{
    // Configura los datos para la habitación de estar
    RoomData livingRoom = {{0.0, 0.0, 0}, LED_BUILTIN, 0, 0};
    roomMap["living"] = livingRoom;

    // Inicializa la comunicación serial
    Serial.begin(9600);

    // Configura el pin de la luz de la habitación de estar como salida
    pinMode(livingRoom.lightPin, OUTPUT);
    digitalWrite(livingRoom.lightPin, HIGH);

    // Conexión WiFi

      // Configures static IP address
    if (!WiFi.config(local_IP, gateway, subnet)) {
        Serial.println("STA Failed to configure");
    }
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
    server.on("/applyData", handleRooms);
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

void handleRooms()
{
    // Leer datos desde el puerto serie
    JsonObject data;
    String source = server.arg("plain");

    if (readJsonFromSource(source, data))
    {
        // Procesar los datos recibidos del puerto serie
        handleLights("living", data);
    }
}


void handleLights(String room, JsonObject &data)
{   
    Serial.println("manejo luces");
    // Control living room lights based on the JSON data
    if (data[room]["lights"].as<String>() == "on")
    {
        digitalWrite(roomMap[room].lightPin, LOW);
    }
    else
    {
        digitalWrite(roomMap[room].lightPin, HIGH);
    }
    //TODO: send response to client in other side
    server.send(200, "text/plain", data[room]["lights"].as<String>());
}

void loop()
{   
    if (Serial.available() > 0)
    {
        // Leer datos desde el puerto serie
        JsonObject data;
        String source = Serial.readStringUntil('\n');
        if (readJsonFromSource(source, data))
        {
            Serial.println("LLega la data");
            // Procesar los datos recibidos del puerto serie
            handleLights("living", data);
        }
    }
    else
    {
        // No hay datos en el puerto serie, intenta desde el servidor web
        server.handleClient();
    }
}
