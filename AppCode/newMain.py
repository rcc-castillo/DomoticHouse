########################################################################
## IMPORTS
########################################################################
import sys, json
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QIcon
from PySide2.QtCore import QTimer, QPropertyAnimation, QTime

########################################################################
# IMPORT GUI FILE AND ROOM CLASS
from ui_DomoticApp import Ui_MainWindow
from Room import Room
from Wifi import Wifi
from SerialConnection import SerialConnection
from RoomUi import RoomUi
########################################################################

SERVER_URL = 'http://192.168.35.249/'
ENDPOINTS = {
    "getData": "getData",
    "getRooms": "getRooms",
    "Lights": "sendLights",
    "Blinds": "sendBlinds",
    "Air": "sendAir",
    "AirSpeed": "sendAir",
    "Irrigation": "sendIrrigation",
    "IrrigationStartTime": "sendIrrigation",
    "IrrigationEndTime": "sendIrrigation"
}

########################################################################
## MAIN WINDOW CLASS
########################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rooms = {}

        self.initUI()

        self.wifi = Wifi(SERVER_URL)
        self.serial = SerialConnection()

        self.dataTimer = QTimer() 
        self.dataTimer.timeout.connect(self.getData)

        self.roomsTimer = QTimer()
        self.roomsTimer.start(100)
        self.roomsTimer.timeout.connect(self.getRooms)

        self.show()
    
    def initUI(self):
        self.setWindowTitle("Domotic App")
        self.setWindowIcon(QIcon(":/icons/icons/window-icon.ico"))
        self.changePage("settings")
        
        #Set connection method button function
        self.ui.setConectionMethod.clicked.connect(self.changeConnectionMethod)
        
        #Set left menu buttons functions
        self.ui.menuBtn.clicked.connect(self.toggleMenu)
        self.ui.livingroomBtn.clicked.connect(lambda: self.changePage("livingroom"))
        self.ui.gardenBtn.clicked.connect(lambda: self.changePage("garden"))
        self.ui.settingsBtn.clicked.connect(lambda: self.changePage("settings"))
        self.ui.livingRoomLightsBtn.setCheckable(True)
        self.ui.livingRoomAirBtn.setCheckable(True)
        self.ui.gardenIrrigationBtn.setCheckable(True)
        self.ui.livingRoomBlindsDownBtn.hide()

        # Set serial connection
        self.ui.disconnectBtn.hide()
        self.ui.updateBtn.clicked.connect(self.updatePorts)
        self.ui.connectBtn.clicked.connect(self.serialConnect)
        self.ui.disconnectBtn.clicked.connect(self.serialDisconnect)
    
    def toggleMenu(self):
        menuCollapsedWidth = 55
        menuExpandedWidth = 155
        isCollapsed = self.ui.leftMenuContainer.width() == menuCollapsedWidth
        width = menuExpandedWidth if isCollapsed else menuCollapsedWidth
        iconPath = ":/icons/icons/chevron-left.svg" if isCollapsed else ":/icons/icons/menu.svg"
        self.ui.menuBtn.setIcon(QIcon(iconPath))
        self.animation = QPropertyAnimation(self.ui.leftMenuContainer, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(self.ui.leftMenuContainer.width())
        self.animation.setEndValue(width)
        self.animation.start()

    def changePage(self, pageName):
        self.ui.mainPages.setCurrentWidget(self.getUiElement(pageName, "", "Page"))
        for button in ["livingroom", "garden", "settings"]:
            style = u"background-color: #52a5e0;" if button == pageName else u"background-color: transparent;"
            self.getUiElement(button, "", "Btn").setStyleSheet(style)
    
    def updatePorts(self):
        self.ui.serial_ports_list.clear()
        self.ui.serial_ports_list.addItems(self.serial.getPorts())
        self.ui.baudrates_list.setCurrentText("9600")
    
    def serialConnect(self):
        self.serial.open(self.ui.serial_ports_list.currentText(), 9600)
        if not self.serial.connected: return
        self.ui.connectBtn.hide()
        self.ui.disconnectBtn.show()
    
    def serialDisconnect(self):
        self.serial.close()
        self.ui.connectBtn.show()
        self.ui.disconnectBtn.hide()
    
    def changeConnectionMethod(self):
        if self.wifi.connected:
            self.serialDisconnect()
            self.ui.setConectionMethod.setText("Cambiar a Serial")
        else:
            self.ui.setConectionMethod.setText("Cambiar a Wifi")
        self.wifi.connected = not self.wifi.connected
        self.ui.serialPortConection.setVisible(not self.wifi.connected)
    
    def getRooms(self):
        if self.wifi.connected:
            data = self.wifi.get(ENDPOINTS["getRooms"])
        elif self.serial.connected:
            data = self.serial.get("getRooms")
        else: return
        
        if data is None: return print("No se pudo obtener la habitación")
        self.roomsTimer.stop()
        self.updateRooms(data)
        # self.serial.clear()
        # self.dataTimer.start(100)
        for roomName in self.rooms:
            room = self.rooms[roomName]["roomObject"]
            
    
    def getData(self):
        if self.wifi.connected:
            data = self.wifi.get(ENDPOINTS["getData"])
        elif self.serial.connected:
            data = self.serial.get("getData")
        else: return
        
        if data is None: return print("No se pudo obtener la data")
        self.updateHumidityTemperature(data)

    def updateRooms(self, data):
        for roomName, roomData in data.items():
            room = Room(name=roomName, **roomData)
            roomUi = RoomUi(room, self.ui)
            self.rooms[roomName] = {"roomObject": room, "roomUi": roomUi}
            for element in roomData:
                roomUi.updateRoomUi(element.capitalize())
        
    def updateHumidityTemperature(self, data):
        for roomName in data:
            room = self.rooms[roomName]["roomObject"]
            roomUi = self.rooms[roomName]["roomUi"]
            room.handleHumidTemp(data[roomName])
            roomUi.updateRoomUi("Humidtemp")
    
    def getUiElement(self, roomName, roomElement, uiElement):
        return getattr(self.ui, f"{roomName}{roomElement.capitalize()}{uiElement}")
    
    def initButton(self, roomName, roomElement, uiElement):
        uiElement.clicked.connect(lambda: self.handleRoomElement(roomName, roomElement, uiElement))
    
    def initComboBox(self, roomName, roomElement, uiElement):
        uiElement.currentTextChanged.connect(lambda: self.handleRoomElement(roomName, roomElement, uiElement))
    
    def initTimeEdit(self, roomName, roomElement, uiElement):
        uiElement.timeChanged.connect(lambda: self.handleRoomElement(roomName, roomElement, uiElement))
    
    def initRoomButtons(self):
        for roomName in self.rooms:
            room = self.rooms[roomName]["roomObject"]
            if room.getElement("lights") is not None:
                element = "Lights"
                uiElement = self.getUiElement(roomName, element, "Btn")
                self.initButton(roomName, element, uiElement)
                
            if room.getElement("blinds") is not None:
                element = "Blinds"
                uiElement = self.getUiElement(roomName, element, "UpBtn")
                self.initButton(roomName, element, uiElement)

                uiElement = self.getUiElement(roomName, element, "DownBtn")
                self.initButton(roomName, element, uiElement)
                
            if room.getElement("air") is not None:
                element = "Air"
                uiElement = self.getUiElement(roomName, element, "Btn")
                self.initButton(roomName, element, uiElement)

                uiElement = self.getUiElement(roomName, element, "Speed")
                self.initComboBox(roomName, f"{element}Speed", uiElement)

            if room.getElement("irrigation") is not None:
                element = "Irrigation"
                uiElement = self.getUiElement(roomName, element, "Btn")
                self.initButton(roomName, element, uiElement)

                uiElement = self.getUiElement(roomName, element, "StartTime")
                self.initTimeEdit(roomName, f"{element}StartTime", uiElement)

                uiElement = self.getUiElement(roomName, element, "EndTime")
                self.initTimeEdit(roomName, f"{element}EndTime", uiElement)

    def handleRoomElement(self, roomName, element, uiElement):
        room = self.rooms[roomName]["roomObject"]
        roomUi = self.rooms[roomName]["roomUi"]

        roomElement = room.getElement(element)
        if element in ["Lights", "Air", "Irrigation"]:
            data = "on" if roomElement["state"] == "off" else "off"
        if element == "Blinds":
            data = "up" if roomElement["state"] == "down" else "down"
        if "Speed" in element:
            data = uiElement.currentText().lower()
        if "Time" in element:
            data = uiElement.time().toString("HH:mm")

        room.getHandler(element)(data)
        roomUi.updateRoomUi(element)
        self.sendData(roomName, element, data)
    
    def sendData(self, roomName, element, data):
        print(f"Sending {element} {data} to {roomName}")
        json_data = json.dumps({roomName: {element: data.lower()}})
        if self.wifi.connected:
            self.wifi.post(f"{ENDPOINTS[element]}?roomName={roomName}&element={element}", json_data)
        elif self.serial.connected:
            self.serial.write(f"{roomName},{element},{json_data}".encode())
        else:print("No hay conexión")


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
