from PySide2 import QtGui
class Room():
    def __init__(self, name, window, lights=None, blinds=None, air=None, humidTemp=None,irrigation=None):
        self.name = name
        self.lights = lights
        self.blinds = blinds
        self.air = air
        self.irrigation = irrigation
        self.humidTemp = humidTemp
        self.window = window
        self.setupUi()

    def handleLights(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        if self.lights["btn"].isChecked():
            self.lights["status"] = "on"
            self.lights["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
            self.lights["btn"].setText("On")
        else:
            self.lights["status"] = "off"
            self.lights["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
            self.lights["btn"].setText("Off")
        self.window.sendData({self.name: {"lights": self.lights["status"]}})
    
    def handleBlinds(self, direction):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        if self.blinds == direction: return
        if self.blinds == "down" and direction == "up":
            self.blinds = direction
        elif self.blinds == "up" and direction == "down":
            self.blinds = direction
        self.window.sendData({self.name: {"blinds": self.blinds}})
    
    def handleAir(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return        
        if self.air["btn"].isChecked():
            self.air["status"] = "on"
            self.air["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
            self.air["btn"].setText("On")
        else:
            self.air["status"] = "off"
            self.air["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
            self.air["btn"].setText("Off")
        self.window.sendData({self.name: {"airState": self.air["status"]}})

    def handleAirSpeed(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        self.air["speedStatus"] = self.air["speedSelector"].currentText()
        self.window.sendData({self.name: {"airSpeed": self.air["speedStatus"].lower()}})
    
    def handleIrrigation(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        if self.irrigation["btn"].isChecked():
            self.irrigation["status"] = "on"
            self.irrigation["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
            self.irrigation["btn"].setText("On")
        else:
            self.irrigation["status"] = "off"
            self.irrigation["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
            self.irrigation["btn"].setText("Off")
        self.window.sendData({self.name: {"irrigationState": self.irrigation["status"]}})

    def handleIrrigationStartTime(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        time = self.irrigation["startTimeSelector"].time()
        self.irrigation["startTime"] = time.toString("HH:mm")
        self.window.sendData({self.name: {"irrigationStartTime": self.irrigation["startTime"]}})
    
    def handleIrrigationEndTime(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        time = self.irrigation["endTimeSelector"].time()
        self.irrigation["endTime"] = time.toString("HH:mm")
        self.window.sendData({self.name: {"irrigationEndTime": self.irrigation["endTime"]}})

    def handleHumidTemp(self, temperature, humidity):
        self.humidTemp["temperature"] = temperature
        self.humidTemp["humidity"] = humidity
        self.humidTemp["temperatureLabel"].setText(str(temperature) + "°C")
        self.humidTemp["humidityLabel"].setText(str(humidity) + "%")

    def setupUi(self):
        print(self.air)
        if self.lights is not None:
            if self.lights["status"] == "on":
                self.lights["btn"].setChecked(True)
                self.lights["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
                self.lights["btn"].setText("On")
            else:
                self.lights["btn"].setChecked(False)
                self.lights["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
                self.lights["btn"].setText("Off")

        if self.air is not None:
            if self.air["status"] == "on":
                self.air["btn"].setChecked(True)
                self.air["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
                self.air["btn"].setText("On")
            else:
                self.air["btn"].setChecked(False)
                self.air["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
                self.air["btn"].setText("Off")
            self.air["speedSelector"].setCurrentText(self.air["speedStatus"].capitalize())

        if self.irrigation is not None:
            if self.irrigation["status"] == "on":
                self.irrigation["btn"].setChecked(True)
                self.irrigation["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
                self.irrigation["btn"].setText("On")
            else:
                self.irrigation["btn"].setChecked(False)
                self.irrigation["btn"].setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
                self.irrigation["btn"].setText("Off")
            self.irrigation["startTimeSelector"].setTime(self.irrigation["startTime"])
            self.irrigation["endTimeSelector"].setTime(self.irrigation["endTime"])
        
        if self.humidTemp is not None:
            self.humidTemp["temperatureLabel"].setText(str(self.humidTemp["temperature"]) + "°C")
            self.humidTemp["humidityLabel"].setText(str(self.humidTemp["humidity"]) + "%")

    def getData(self):
        return {
            self.name: 
                {"lights": self.lights["status"], 
                 "blinds": self.blinds,
                 "air": {"state": self.air["status"],
                         "speed": self.air["speedStatus"].lower()}}
            }
    