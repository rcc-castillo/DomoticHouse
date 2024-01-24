from Room import Room
from RoomUi import RoomUi
class RoomController:
    def __init__(self, ui, communicationController):
        self.rooms = {}
        self.ui = ui
        self.communicationController = communicationController

    def updateRooms(self, data):
        for roomName, roomData in data.items():
            room = Room(name=roomName, **roomData)
            roomUi = RoomUi(room, self.ui)
            self.rooms[roomName] = {"roomObject": room, "roomUi": roomUi}
            for deviceName in roomData:
                roomUi.updateRoomUi(deviceName.capitalize())
    
    def updateHumidityTemperature(self, data):
        for roomName in data:
            room = self.rooms[roomName]["roomObject"]
            roomUi = self.rooms[roomName]["roomUi"]
            room.handleHumidTemp(data[roomName])
            roomUi.updateRoomUi("Humidtemp")

    def initButton(self, roomName, deviceName, deviceElement, uiElement):
        uiElement.clicked.connect(lambda: self.handleRoomDevice(roomName, deviceName, deviceElement, uiElement))

    def initComboBox(self, roomName, deviceName, deviceElement, uiElement):
        uiElement.currentTextChanged.connect(lambda: self.handleRoomDevice(roomName, deviceName, deviceElement, uiElement))

    def initTimeEdit(self, roomName, deviceName, deviceElement, uiElement):
        uiElement.timeChanged.connect(lambda: self.handleRoomDevice(roomName, deviceName, deviceElement, uiElement))

    def initRoomButtons(self):
        for roomName in self.rooms:
            room = self.rooms[roomName]["roomObject"]
            roomUi = self.rooms[roomName]["roomUi"]
            self.initRoomUiElements(roomName, room, roomUi)

    def initRoomUiElements(self, roomName, room, roomUi):
        elements = [("Lights", "Btn"), ("Blinds", "UpBtn"), ("Blinds", "DownBtn"), 
                    ("Air", "Btn"), ("Air", "Speed"), ("Irrigation", "Btn"), 
                    ("Irrigation", "StartTime"), ("Irrigation", "EndTime")]

        for deviceName, uiType in elements:
            if room.getDevice(deviceName) is not None:
                uiElement = roomUi.getUiElement(roomName, deviceName, uiType)
                if uiType in ["Btn", "UpBtn", "DownBtn"]:
                    deviceElement = "State"
                    self.initButton(roomName, deviceName, deviceElement, uiElement)
                elif uiType == "Speed":
                    deviceElement = "Speed"
                    self.initComboBox(roomName, deviceName, deviceElement, uiElement)
                elif uiType in ["StartTime", "EndTime"]:
                    deviceElement = uiType
                    self.initTimeEdit(roomName, deviceName, deviceElement, uiElement)

    def handleRoomDevice(self, roomName, deviceName, deviceElement, uiElement):
        if not self.communicationController.wifiIsConnected() and not self.communicationController.serialIsConnected():
            return
        room = self.rooms[roomName]["roomObject"]
        roomUi = self.rooms[roomName]["roomUi"]
        data = self.getDeviceData(room, deviceName, deviceElement, uiElement)
        room.getHandler(deviceName, deviceElement)(data)
        roomUi.updateRoomUi(deviceName.capitalize())
        self.communicationController.sendData(roomName, deviceName, deviceElement, data)

    def getDeviceData(self, room, deviceName, deviceElement, uiElement):
        deviceData = room.getDevice(deviceName)
        if deviceElement == "Speed":
            return uiElement.currentText().lower()
        elif "Time" in deviceElement:
            return uiElement.time().toString("HH:mm")
        elif deviceElement == "State":
            if deviceName == "Blinds":
                return "up" if deviceData["state"] == "down" else "down"
            return "on" if deviceData["state"] == "off" else "off"
    
    