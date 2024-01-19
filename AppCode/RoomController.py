class RoomController:
    def __init__(self, rooms):
        self.rooms = rooms

    def initButton(self, roomName, roomElement, uiElement):
        uiElement.clicked.connect(lambda: self.handleRoomElement(roomName, roomElement, uiElement))

    def initComboBox(self, roomName, roomElement, uiElement):
        uiElement.currentTextChanged.connect(lambda: self.handleRoomElement(roomName, roomElement, uiElement))

    def initTimeEdit(self, roomName, roomElement, uiElement):
        uiElement.timeChanged.connect(lambda: self.handleRoomElement(roomName, roomElement, uiElement))

    def initRoomButtons(self):
        for roomName in self.rooms:
            room = self.rooms[roomName]["roomObject"]
            roomUi = self.rooms[roomName]["roomUi"]
            self.initRoomElements(roomName, room, roomUi)

    def initRoomElements(self, roomName, room, roomUi):
        elements = [("lights", "Btn"), ("blinds", "UpBtn"), ("blinds", "DownBtn"), 
                    ("air", "Btn"), ("air", "Speed"), ("irrigation", "Btn"), 
                    ("irrigation", "StartTime"), ("irrigation", "EndTime")]

        for element, uiType in elements:
            if room.getElement(element) is not None:
                uiElement = roomUi.getUiElement(roomName, element, uiType)
                if uiType == "Btn":
                    self.initButton(roomName, element, uiElement)
                elif uiType == "Speed":
                    self.initComboBox(roomName, f"{element}Speed", uiElement)
                elif uiType in ["StartTime", "EndTime"]:
                    self.initTimeEdit(roomName, f"{element}{uiType}", uiElement)

    def handleRoomElement(self, roomName, element, uiElement):
        room = self.rooms[roomName]["roomObject"]
        roomUi = self.rooms[roomName]["roomUi"]

        roomElement = room.getElement(element)
        data = self.getElementData(element, roomElement, uiElement)

        room.getHandler(element)(data)
        roomUi.updateRoomUi(element)
        self.sendData(roomName, element, data)

    def getElementData(self, element, roomElement, uiElement):
        if element in ["Lights", "Air", "Irrigation"]:
            return "on" if roomElement["state"] == "off" else "off"
        elif element == "Blinds":
            return "up" if roomElement["state"] == "down" else "down"
        elif "Speed" in element:
            return uiElement.currentText().lower()
        elif "Time" in element:
            return uiElement.time().toString("HH:mm")