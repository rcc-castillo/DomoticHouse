#ifndef Irrigation_h
#define Irrigation_h

#include <Arduino.h>
#include "Device.h"

class Irrigation : public Device{
    private:
        bool _irrigationEnabled;
        String _irrigationState;
        std::tuple<int, int> _irrigationStartTime;
        std::tuple<int, int> _irrigationEndTime;
        void init() override;
    
    public:
        Irrigation(int pin, const String &name);
        String get(const String &deviceElement) override;
        void set(const String &deviceElement, const String &data) override;
        String getIrrigationStartTime();
        String getIrrigationEndTime();
        void setIrrigationState(const String &data);
        void setIrrigationStartTime(const String &data);
        void setIrrigationEndTime(const String &data);
        void handleProgrammedCommand(const String &command, int currentHour, int currentMinute) override;
};
#endif