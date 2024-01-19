#include "ReadJson.h"

bool readJsonFromSource(const String &source, JsonObject &data)
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