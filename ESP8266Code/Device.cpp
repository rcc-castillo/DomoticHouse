#include "Device.h"

Device::Device(int pin, const String &name) {
    _pin = pin;
    _name = name;
}

String Device::getName() {
  return String();
}
