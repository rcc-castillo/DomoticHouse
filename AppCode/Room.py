from PySide2 import QtGui
class Room():
    def __init__(self, name, lights, blinds, air, window):
        self.name = name
        self.lights = lights
        self.blinds = blinds
        self.air = air
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
        self.window.sendData(self.getData())
    
    def handleBlinds(self, direction):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        if self.blinds == direction: return
        if self.blinds == "down" and direction == "up":
            self.blinds = direction
        elif self.blinds == "up" and direction == "down":
            self.blinds = direction
        self.window.sendData(self.getData())
    
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
        self.window.sendData(self.getData())

    def handleAirSpeed(self):
        if not self.window.serial.isOpen() and not self.window.uisingWifi:
            return
        self.air["speedStatus"] = self.air["speedOptions"].currentText()
        self.window.sendData(self.getData())

    def getData(self):
        return {
            self.name: 
                {"lights": self.lights["status"], 
                 "blinds": self.blinds,
                 "air": {"state": self.air["status"],
                         "speed": self.air["speedStatus"].lower()}}
            }
    