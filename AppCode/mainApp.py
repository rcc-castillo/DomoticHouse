########################################################################
## IMPORTS
########################################################################
import sys, json, requests
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui
from PySide2.QtSerialPort import QSerialPort, QSerialPortInfo

########################################################################
# IMPORT GUI FILE AND ROOM CLASS
from ui_DomoticApp import *
from Room import *
########################################################################

SERVER_URL = 'http://192.168.252.249/'

########################################################################
## MAIN WINDOW CLASS
########################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()

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
        self.timer.timeout.connect(self.wifiRead)

        #Init rooms
        self.initRooms()
        self.initLivingRoom()
        self.initGarden()

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

    def initRooms(self):
        url = SERVER_URL + "getRooms"
        response = requests.get(url)
        if response.status_code != 200: 
            return f"Failed to get rooms from server. Status code: {response.status_code}"
        data = json.loads(response.text)
        self.merge_dicts(data, self.roomUIElements)

        self.rooms = {}
        for roomName, roomData in data.items():
            lights = roomData.get("lights")
            blinds = roomData.get("blinds")
            air = roomData.get("air")
            irrigation = roomData.get("irrigation")
            humidTemp = roomData.get("humidTemp")

            if irrigation is not None:
                print(irrigation)
                irrigation["startTime"] = QTime.fromString(irrigation["startTime"], 'hh:mm')
                irrigation["endTime"] = QTime.fromString(irrigation["endTime"], 'hh:mm')

            self.rooms[roomName] = Room(name=roomName, lights=lights, blinds=blinds, air=air, irrigation=irrigation, humidTemp=humidTemp, window=self)
        
    def initSerial(self):
        self.ui.disconnectBtn.hide()
        self.serial = QSerialPort()
        self.ui.updateBtn.clicked.connect(self.readPorts)
        self.ui.connectBtn.clicked.connect(self.serialConnect)
        self.ui.disconnectBtn.clicked.connect(lambda: self.serialDisconnect())
        self.serial.readyRead.connect(self.serialRead)
    
    def initLivingRoom(self):
        self.livingRoom = self.rooms["livingRoom"]
        #Set room lights buttons functions
        self.ui.livingLightsBtn.clicked.connect(
            lambda: self.livingRoom.handleLights())

        #Set room blinds buttons functions
        self.ui.livingBlindUpBtn.clicked.connect(
            lambda: self.livingRoom.handleBlinds("up"))
        self.ui.livingBlindDownBtn.clicked.connect(
            lambda: self.livingRoom.handleBlinds("down"))
        
        #Set room air conditioner buttons functions
        self.ui.livingAirBtn.clicked.connect(
            lambda: self.livingRoom.handleAir())
        
        #Set air conditioner speed
        self.ui.livingAirSpeed.currentTextChanged.connect(
            lambda: self.livingRoom.handleAirSpeed())
    
    def initGarden(self):
        self.garden = self.rooms["garden"]
        self.ui.irrigationBtn.clicked.connect(
            lambda: self.garden.handleIrrigation())
        
        # Irrigation start time
        self.ui.irrigationStartTime.editingFinished.connect(
            lambda: self.garden.handleIrrigationStartTime())
        
                # Irrigation start time
        self.ui.irrigationEndTime.editingFinished.connect(
            lambda: self.garden.handleIrrigationEndTime())
        
    ########################################################################
    ## Functions refred to GUI functions
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
            data = json.loads(line)
            self.updateUI(data)
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
            self.wifiSend(json_data)
        else:
            print("No hay conexión")

    def wifiSend(self, data):
        """
        Sends the data to the wifi
        """
        url = SERVER_URL + "sendData"
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        response = requests.post(url, headers=headers, data=data)
        print(response.status_code)
        print(response.text)

    def wifiRead(self):
        """
        Reads the data from the wifi
        """
        if not self.uisingWifi: return
        url = SERVER_URL + "getData"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.updateUI(data)
        else:
            print(f"Failed to get data from server. Status code: {response.status_code}")
    
    def updateUI(self, data):
        """
        Updates the UI with the data from the wifi or serial port
        """
        for room in data:
            self.rooms[room]
            temperature = data[room]["temperature"]
            humidity = data[room]["humidity"]
            self.rooms[room].handleHumidTemp(temperature, humidity)

    def merge_dicts(self, d1, d2):
        for key in d2:
            if key in d1 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
                self.merge_dicts(d1[key], d2[key])
            else:
                d1[key] = d2[key]

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
