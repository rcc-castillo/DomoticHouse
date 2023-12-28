########################################################################
## IMPORTS
########################################################################
import sys, json
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui
from PySide2.QtSerialPort import QSerialPort, QSerialPortInfo

########################################################################
# IMPORT GUI FILE AND ROOM CLASS
from ui_DomoticApp import *
from Room import *
from Wifi import *
########################################################################

SERVER_URL = 'http://192.168.34.249/'

########################################################################
## MAIN WINDOW CLASS
########################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.wifi = Wifi(SERVER_URL)

        #Utils variables for window functions
        self.buttonGroupPages = { 
            "livingroom" : [self.ui.livingroomPage, self.ui.livingroomBtn],
            "garden" : [self.ui.gardenPage, self.ui.gardenBtn], 
            "settings" : [self.ui.settingsPage, self.ui.settingsBtn]}
        self.menuCollapsedWidth = 55
        self.menuExpandedWidth = 155
        self.uisingWifi = False
        self.roomUIElements = {
            "livingRoom": {
                "lights": {"btn": self.ui.livingLightsBtn},
                "blinds": {"upBtn": self.ui.livingBlindUpBtn, "downBtn": self.ui.livingBlindDownBtn},
                "air": {"btn": self.ui.livingAirBtn, "speedSelector": self.ui.livingAirSpeed},
                "humidTemp": {"humidityLabel": self.ui.livingHumidityLbl, "temperatureLabel": self.ui.livingTemperatureLbl}
            },
            "garden": {
                "irrigation": {"btn": self.ui.irrigationBtn, "startTimeSelector": self.ui.irrigationStartTime, "endTimeSelector": self.ui.irrigationEndTime}
            }
        }
        
        #Init UI, Serial and wifiRead
        self.configureUI()
        self.initSerial()
        self.timer.start(1000)
        self.timer.timeout.connect(self.getData)

        #Init roomss
        self.getRooms()
        self.initRooms()

        self.show() 

    def configureUI(self):
        self.setWindowTitle("Domotic App")
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/window-icon.ico"))
        self.changePage("settings")
        
        #Set connection method button function
        self.ui.setConectionMethod.clicked.connect(self.changeConnectionMethod)
        
        #Set left menu buttons functions
        self.ui.menuBtn.clicked.connect(self.toggleMenu)
        self.ui.livingroomBtn.clicked.connect(lambda: 
                                            self.changePage("livingroom"))
        self.ui.gardenBtn.clicked.connect(lambda: self.changePage("garden"))
        self.ui.settingsBtn.clicked.connect(lambda: self.changePage("settings"))
        self.ui.livingLightsBtn.setCheckable(True)
        self.ui.livingAirBtn.setCheckable(True)
        self.ui.irrigationBtn.setCheckable(True)

    def getRooms(self):
        data = self.wifi.get("getRooms")
        if data is None: return

        self.rooms = {}
        for roomName, roomData in data.items():
            self.rooms[roomName] = Room(name=roomName, window=self, **roomData)
            for element in roomData:
                self.updateUi(roomName, element, self.rooms[roomName].getElement(element))
        
    def initSerial(self):
        self.ui.disconnectBtn.hide()
        self.serial = QSerialPort()
        self.ui.updateBtn.clicked.connect(self.readPorts)
        self.ui.connectBtn.clicked.connect(self.serialConnect)
        self.ui.disconnectBtn.clicked.connect(lambda: self.serialDisconnect())
        self.serial.readyRead.connect(self.serialRead)
    
    def initRooms(self):
        for roomName in self.rooms:
            roomUI = self.roomUIElements[roomName]
            handlers = {
                "blinds": self.connectBlindsButtons,
                "lights": self.connectLightsButton,
                "air": self.connectAirButtons,
                "irrigation": self.connectIrrigationButtons
            }
            for element, ui in roomUI.items():
                if element in handlers:
                    handlers[element](ui, roomName)

    def connectBlindsButtons(self, ui, roomName):
            btnUp = ui["upBtn"]
            btnUp.clicked.connect(lambda: self.handleRoom(roomName, "blinds"))
            
            btnDown = ui["downBtn"]
            btnDown.clicked.connect(lambda: self.handleRoom(roomName, "blinds"))

    def connectLightsButton(self, ui, roomName):
        btn = ui["btn"]
        btn.clicked.connect(lambda: 
            self.handleRoom(roomName, "lights"))

    def connectAirButtons(self, ui, roomName):
        btn = ui["btn"]
        btn.clicked.connect(lambda: self.handleRoom(roomName, "air"))

        speedSelector = ui["speedSelector"]
        speedSelector.currentTextChanged.connect(lambda: 
            self.handleRoom(roomName, "airSpeed", speedSelector))

    def connectIrrigationButtons(self, ui, roomName):
        btn = ui["btn"]
        btn.clicked.connect(lambda: self.handleRoom(roomName, "irrigation"))

        startTimeSelector = ui["startTimeSelector"]
        startTimeSelector.editingFinished.connect(lambda: self.handleRoom(roomName, "irrigationStartTime", startTimeSelector))
        
        endTimeSelector = ui["endTimeSelector"]
        endTimeSelector.editingFinished.connect(lambda: self.handleRoom(roomName, "irrigationEndTime", endTimeSelector))
    
    ########################################################################
    ## Functions refred to GUI functionality
    ########################################################################
    def toggleMenu(self):
        """
        Toggles the visibility of the left menu container by animating its
        width and change menu button. 
        """
        if self.ui.leftMenuContainer.width() == self.menuCollapsedWidth:
            width = self.menuExpandedWidth
            self.ui.menuBtn.setIcon(QtGui.QIcon(":/icons/icons/chevron-left.svg"))
        else:
            width = self.menuCollapsedWidth
            self.ui.menuBtn.setIcon(QtGui.QIcon(":/icons/icons/menu.svg"))
        self.animation = QPropertyAnimation(self.ui.leftMenuContainer, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(self.ui.leftMenuContainer.width())
        self.animation.setEndValue(width)
        self.animation.start()

    def changePage(self, pageName):
        """
        Changes the current page of the application to the specified page.

        Args:
            pageName (str): The name of the page to switch to.
        """
        self.ui.mainPages.setCurrentWidget(self.buttonGroupPages[pageName][0])
        for button in self.buttonGroupPages:
            self.buttonGroupPages[button][1].setStyleSheet(u"background-color: transparent;")
        self.buttonGroupPages[pageName][1].setStyleSheet(u"background-color: #52a5e0;")

    ########################################################################
    ## Functions refred to comunications
    ########################################################################
    def changeConnectionMethod(self):
        """
        Changes the connection method between wifi and serial port.
        """
        if self.uisingWifi:
            self.ui.serialPortConection.show()
            self.ui.setConectionMethod.setText("Cambiar a Wifi")
            self.uisingWifi = False
        else:
            self.ui.serialPortConection.hide()
            self.serialDisconnect()
            self.ui.setConectionMethod.setText("Cambiar a Serial")
            self.uisingWifi = True

    def readPorts(self):
        """
        Reads all available serial ports and add them to the ports combobox
        """
        self.ui.serial_ports_list.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.ui.serial_ports_list.addItem(port.portName())
        self.ui.baudrates_list.setCurrentText("9600")

    def serialConnect(self):
            """
            Connects to the serial port selected in the ports combobox.
            Sets the port name and baudrate, opens the serial port for reading and writing.
            Hides the connect button and shows the disconnect button if the serial port is successfully opened.
            """
            port = self.ui.serial_ports_list.currentText()
            baudrate = int(self.ui.baudrates_list.currentText())
            self.serial.setPortName(port)
            self.serial.setBaudRate(baudrate)
            self.serial.open(QIODevice.ReadWrite)
            if self.serial.isOpen():
                self.ui.connectBtn.hide()
                self.ui.disconnectBtn.show()

    def serialDisconnect(self):
        """
        Disconnects from the serial port and updates the UI accordingly.
        """
        self.serial.close()
        if not self.serial.isOpen():
            self.ui.connectBtn.show()
            self.ui.disconnectBtn.hide()

    def serialRead(self):
        """
        Reads the serial port and returns the data
        """
        if not self.serial.isOpen() or not self.serial.canReadLine(): return
        line = self.serial.readLine().data().decode().strip()
        print(line)
        if line.startswith('{') and line.endswith('}'):
            self.updateHumidityTemperature(json.loads(line))
        else:
            print(line)       
        
    def sendData(self, data):
        """
        Sends the data to the serial port
        """
        print("Datos enviados: ", data)
        json_data = json.dumps(data)

        if self.serial.isOpen():
            self.serial.write(json_data.encode())
        elif self.uisingWifi:
            self.wifi.post("sendData", json_data)
        else:
            print("No hay conexión")

    def getData(self):
        """
        Reads the data from server
        """
        if self.serial.isOpen():
            self.serialRead()
        elif self.uisingWifi:
            data = self.wifi.get("getData")
            if data is None: return
            self.updateHumidityTemperature(data)
        else:
            print("No hay conexión")

    def updateHumidityTemperature(self, data):
        """
        Updates the UI with the data from the wifi or serial port
        """
        for room in data:
            self.rooms[room]
            temperature = data[room]["temperature"]
            humidity = data[room]["humidity"]
            self.rooms[room].handleHumidTemp(temperature, humidity)
            self.updateUi(room, "humidTemp", {"temperature": temperature, "humidity": humidity})

    def determineState(self, room, element, data):
        if element in ["lights", "air", "irrigation"] and data is None:
            return "on" if room.getElement(element)["state"] == "off" else "off"
        if element == "blinds" and data is None:
            return "up" if room.getElement(element)["state"] == "down" else "down"
        if element == "airSpeed":
            return data.currentText()
        if element in ["irrigationStartTime", "irrigationEndTime"]:
            return data.time().toString('HH:mm')
        
    def handleRoom(self, roomName, element, data=None):
        if not self.serial.isOpen() and not self.uisingWifi:
            return
        room = self.rooms[roomName]
        handlers = {
            "lights": room.handleLights,
            "blinds": room.handleBlinds,
            "air": room.handleAir,
            "airSpeed": room.handleAirSpeed,
            "irrigation": room.handleIrrigation,
            "irrigationStartTime": room.handleIrrigationStartTime,
            "irrigationEndTime": room.handleIrrigationEndTime
        }

        state = self.determineState(room, element, data)

        if element in handlers:
            handlers[element](state)
        
        self.updateUi(roomName, element, room.getElement(element))
        self.sendData({roomName: {element: state.lower()}})

    def updateUi(self, roomName, element, roomData):
        roomUI = self.roomUIElements[roomName]
        if roomData is None:
            return
        if element in ["lights", "air", "irrigation"]:
            icon_path = ":/icons/icons/toggle-right.svg" if roomData["state"] == "on" else ":/icons/icons/toggle-left.svg"
            roomUI[element]["btn"].setChecked(True)
            roomUI[element]["btn"].setIcon(QtGui.QIcon(icon_path))
            roomUI[element]["btn"].setText(roomData["state"].capitalize())
        
        if element == "blinds":
            if roomData["state"] == "up":
                roomUI[element]["upBtn"].hide()
                roomUI[element]["downBtn"].show()

            elif roomData["state"] == "down":
                roomUI[element]["downBtn"].hide()
                roomUI[element]["upBtn"].show()
        
        if element == "air":
            roomUI[element]["speedSelector"].setCurrentText(roomData["speed"].capitalize())

        if element == "irrigation":
            startTime = QtCore.QTime.fromString(roomData["startTime"], 'HH:mm')
            endTime = QtCore.QTime.fromString(roomData["endTime"], 'HH:mm')
            roomUI[element]["startTimeSelector"].setTime(startTime)
            roomUI[element]["endTimeSelector"].setTime(endTime)

        if element == "humidTemp":
            temperature = roomData["temperature"]
            humidity = roomData["humidity"]
            roomUI[element]["temperatureLabel"].setText(str(temperature) + "°C")
            roomUI[element]["humidityLabel"].setText(str(humidity) + "%")
    
        
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
