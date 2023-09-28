#include <ArduinoJson.h>

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
}

void loop() {
  if (Serial.available()) {
    // Lee los datos JSON del puerto serie
    String jsonStr = Serial.readStringUntil('\n');

    // Crea un objeto JSON para analizar los datos
    StaticJsonDocument<1000> jsonDoc;
    DeserializationError error = deserializeJson(jsonDoc, jsonStr);

    // Verifica si hubo un error al analizar los datos JSON
    if (error) {
      Serial.print("Error al analizar JSON: ");
      Serial.println(error.c_str());
      return;
    }

    // Verifica el estado de las luces en el salón
    String salonLights = jsonDoc["living"]["lights"].as<String>();
    Serial.print(salonLights);

    // Controla el LED incorporado en base al estado de las luces en el salón
    if (salonLights == "on") {
      digitalWrite(LED_BUILTIN, LOW); // Enciende el LED incorporado
    } else {
      digitalWrite(LED_BUILTIN, HIGH); // Apaga el LED incorporado
    }
  }
}