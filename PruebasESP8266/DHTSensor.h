#ifndef DHT11Sensor_h
#define DHT11Sensor_h

#include <Arduino.h>
#include "Device.h"
#include "DHT.h"

class DHTSensor : public Device {
    private:
        int _sensorPin;
        DHT* _dht;
        void init() override;
    
    public:
        DHTSensor(int pin, const String &name);
        String get(const String &deviceElement) override;
        void set(const String &deviceElement, const String &data) override;
        float getTemperature();
        float getHumidity();
        void handleProgrammedCommand(const String &command, int currentHour, int currentMinute) override;
};
#endif