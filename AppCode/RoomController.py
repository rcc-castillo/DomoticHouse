from Room import Room
class RoomController:
    def __init__(self, uiController, communicationController):
        self.rooms = {}
        self.uiController = uiController
        self.communicationController = communicationController

    def updateRooms(self, data):
        for roomName, roomData in data.items():
            room = Room(name=roomName, **roomData)
            self.rooms[roomName] = room
            for deviceName in roomData:
                deviceName = deviceName.capitalize()
                self.uiController.updateRoomUi(roomName, deviceName, room.getDevice(deviceName))
    
    def updateHumidityTemperature(self, data):
        for roomName in data:
            room = self.rooms[roomName]
            room.handleHumidTemp(data[roomName])
            self.uiController.updateRoomUi(roomName, "Humidtemp", room.getDevice("Humidtemp"))

    def initButton(self, roomName, deviceName, deviceElement, uiElement):
        uiElement.clicked.connect(lambda: self.handleRoomDevice(roomName, deviceName, deviceElement, uiElement))

    def initComboBox(self, roomName, deviceName, deviceElement, uiElement):
        uiElement.currentTextChanged.connect(lambda: self.handleRoomDevice(roomName, deviceName, deviceElement, uiElement))

    def initTimeEdit(self, roomName, deviceName, deviceElement, uiElement):
        uiElement.timeChanged.connect(lambda: self.handleRoomDevice(roomName, deviceName, deviceElement, uiElement))

    def initRoomButtons(self):
        for roomName in self.rooms:
            room = self.rooms[roomName]
            self.initRoomUiElements(roomName, room)

    def initRoomUiElements(self, roomName, room):
        elements = [("Lights", "Btn"), ("Blinds", "UpBtn"), ("Blinds", "DownBtn"), 
                    ("Air", "Btn"), ("Air", "Speed"), ("Irrigation", "Btn"), 
                    ("Irrigation", "StartTime"), ("Irrigation", "EndTime")]

        for deviceName, uiType in elements:
            if room.getDevice(deviceName) is not None:
                uiElement = self.uiController.getUiElement(roomName, deviceName, uiType)
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
        room = self.rooms[roomName]
        data = self.getDeviceData(room, deviceName, deviceElement, uiElement)
        room.getHandler(deviceName, deviceElement)(data)
        self.uiController.updateRoomUi(roomName, deviceName.capitalize(), room.getDevice(deviceName.capitalize()))
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
    
    