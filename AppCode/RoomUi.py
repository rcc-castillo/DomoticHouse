from PySide2.QtGui import QIcon 
from PySide2.QtCore import QTime
class RoomUi:
    def __init__(self, room, ui):
        self.room = room
        self.ui = ui
    
    def updateRoomUi(self, deviceName):
        updators = {
            "Lights": self.updateLights,
            "Blinds": self.updateBlinds,
            "Air": self.updateAir,
            "Irrigation": self.updateIrrigation,
            "Humidtemp": self.updateHumidTemp
        }
        updators[deviceName](self.room.name, self.room.getDevice(deviceName))
    
    def getUiElement(self, roomName, roomDevice, uiElement):
        attributeName = f"{roomName}{roomDevice.capitalize()}{uiElement}"
        return getattr(self.ui, attributeName)
    
    def updateLights(self, roomName, deviceData):
        iconPath = ":/icons/icons/toggle-right.svg" if deviceData["state"] == "on" else ":/icons/icons/toggle-left.svg"
        check = True if deviceData["state"] == "on" else False
        self.getUiElement(roomName, "Lights", "Btn").setChecked(check)
        self.getUiElement(roomName, "Lights", "Btn").setIcon(QIcon(iconPath))
        self.getUiElement(roomName, "Lights", "Btn").setText(deviceData["state"].capitalize())
    
    def updateBlinds(self, roomName, deviceData):
        if deviceData["state"] == "up":
            self.getUiElement(roomName, "Blinds", "UpBtn").hide()
            self.getUiElement(roomName, "Blinds", "DownBtn").show()

        elif deviceData["state"] == "down":
            self.getUiElement(roomName, "Blinds", "DownBtn").hide()
            self.getUiElement(roomName, "Blinds", "UpBtn").show()
    
    def updateAir(self, roomName, deviceData):
        iconPath = ":/icons/icons/toggle-right.svg" if deviceData["state"] == "on" else ":/icons/icons/toggle-left.svg"
        check = True if deviceData["state"] == "on" else False
        self.getUiElement(roomName, "Air", "Btn").setChecked(check)
        self.getUiElement(roomName, "Air", "Btn").setIcon(QIcon(iconPath))
        self.getUiElement(roomName, "Air", "Btn").setText(deviceData["state"].capitalize())
        self.getUiElement(roomName, "Air", "Speed").setCurrentText(deviceData["speed"].capitalize())

    def updateIrrigation(self, roomName, deviceData):
        iconPath = ":/icons/icons/toggle-right.svg" if deviceData["state"] == "on" else ":/icons/icons/toggle-left.svg"
        check = True if deviceData["state"] == "on" else False
        self.getUiElement(roomName, "Irrigation", "Btn").setChecked(check)
        self.getUiElement(roomName, "Irrigation", "Btn").setIcon(QIcon(iconPath))
        self.getUiElement(roomName, "Irrigation", "Btn").setText(deviceData["state"].capitalize())
        startTime = QTime.fromString(deviceData["startTime"], 'HH:mm')
        endTime = QTime.fromString(deviceData["endTime"], 'HH:mm')
        self.getUiElement(roomName, "Irrigation", "StartTime").setTime(startTime)
        self.getUiElement(roomName, "Irrigation", "EndTime").setTime(endTime)
    
    def updateHumidTemp(self, roomName, deviceData):
        temperature = deviceData["temperature"]
        humidity = deviceData["humidity"]
        self.getUiElement(roomName, "Humidtemp", "TemperatureLbl").setText(str(temperature) + "°C")
        self.getUiElement(roomName, "Humidtemp", "HumidityLbl").setText(str(humidity) + "%")