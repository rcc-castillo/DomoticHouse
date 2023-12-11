from PySide2 import QtGui
class Room():
    def __init__(self, name, window, lights=None, blinds=None, air=None, irrigation=None):
        self.name = name
        self.lights = lights
        self.blinds = blinds
        self.air = air
        self.irrigation = irrigation
        self.window = window

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
        self.window.sendData({self.name: {"airSpeed": self.air["speedStatus"]}})
    
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
        self.window.sendData({self.name: {"irrigation": self.irrigation["status"]}})

    def handleIrrigationStartTime(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        time = self.irrigation["startTimeSelector"].time()
        self.irrigation["startTime"] = (time.hour(), time.minute())
        self.window.sendData({self.name: {"irrigationStartTime": self.irrigation["startTime"]}})
    
    def handleIrrigationEndTime(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        time = self.irrigation["endTimeSelector"].time()
        self.irrigation["endTime"] = (time.hour(), time.minute())
        self.window.sendData({self.name: {"irrigationEndTime": self.irrigation["endTime"]}})

    def getData(self):
        return {
            self.name: 
                {"lights": self.lights["status"], 
                 "blinds": self.blinds,
                 "air": {"state": self.air["status"],
                         "speed": self.air["speedStatus"].lower()}}
            }
    