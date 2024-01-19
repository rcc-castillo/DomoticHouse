from PySide2.QtGui import QIcon 
from PySide2.QtCore import QTime
class RoomUi:
    def __init__(self, room, ui):
        self.room = room
        self.ui = ui
    
    def updateRoomUi(self, element):
        updators = {
            "Lights": self.updateLights,
            "Blinds": self.updateBlinds,
            "Air": self.updateAir,
            "AirSpeed": self.updateAir,
            "Irrigation": self.updateIrrigation,
            "IrrigationStartTime": self.updateIrrigation,
            "IrrigationEndTime": self.updateIrrigation,
            "Humidtemp": self.updateHumidTemp
        }
        if element in ["IrrigationStartTime", "IrrigationEndTime"]:
            updators["Irrigation"](self.room.name, self.room.getElement("Irrigation"))
        elif element == "AirSpeed":
            updators["Air"](self.room.name, self.room.getElement("Air"))
        else:
            updators[element](self.room.name, self.room.getElement(element))
    
    def getUiElement(self, roomName, roomElement, uiElement):
        attributeName = f"{roomName}{roomElement.capitalize()}{uiElement}"
        return getattr(self.ui, attributeName)
    
    def updateLights(self, roomName, roomData):
        iconPath = ":/icons/icons/toggle-right.svg" if roomData["state"] == "on" else ":/icons/icons/toggle-left.svg"
        check = True if roomData["state"] == "on" else False
        self.getUiElement(roomName, "Lights", "Btn").setChecked(check)
        self.getUiElement(roomName, "Lights", "Btn").setIcon(QIcon(iconPath))
        self.getUiElement(roomName, "Lights", "Btn").setText(roomData["state"].capitalize())
    
    def updateBlinds(self, roomName, roomData):
        if roomData["state"] == "up":
            self.getUiElement(roomName, "Blinds", "UpBtn").hide()
            self.getUiElement(roomName, "Blinds", "DownBtn").show()

        elif roomData["state"] == "down":
            self.getUiElement(roomName, "Blinds", "DownBtn").hide()
            self.getUiElement(roomName, "Blinds", "UpBtn").show()
    
    def updateAir(self, roomName, roomData):
        iconPath = ":/icons/icons/toggle-right.svg" if roomData["state"] == "on" else ":/icons/icons/toggle-left.svg"
        check = True if roomData["state"] == "on" else False
        self.getUiElement(roomName, "Air", "Btn").setChecked(check)
        self.getUiElement(roomName, "Air", "Btn").setIcon(QIcon(iconPath))
        self.getUiElement(roomName, "Air", "Btn").setText(roomData["state"].capitalize())
        self.getUiElement(roomName, "Air", "Speed").setCurrentText(roomData["speed"].capitalize())

    def updateIrrigation(self, roomName, roomData):
        iconPath = ":/icons/icons/toggle-right.svg" if roomData["state"] == "on" else ":/icons/icons/toggle-left.svg"
        check = True if roomData["state"] == "on" else False
        self.getUiElement(roomName, "Irrigation", "Btn").setChecked(check)
        self.getUiElement(roomName, "Irrigation", "Btn").setIcon(QIcon(iconPath))
        self.getUiElement(roomName, "Irrigation", "Btn").setText(roomData["state"].capitalize())
        startTime = QTime.fromString(roomData["startTime"], 'HH:mm')
        endTime = QTime.fromString(roomData["endTime"], 'HH:mm')
        self.getUiElement(roomName, "Irrigation", "StartTime").setTime(startTime)
        self.getUiElement(roomName, "Irrigation", "EndTime").setTime(endTime)
    
    def updateHumidTemp(self, roomName, roomData):
        temperature = round(roomData["temperature"], 2)
        humidity = roomData["humidity"]
        self.getUiElement(roomName, "Humidtemp", "TemperatureLbl").setText(str(temperature) + "°C")
        self.getUiElement(roomName, "Humidtemp", "HumidityLbl").setText(str(humidity) + "%")