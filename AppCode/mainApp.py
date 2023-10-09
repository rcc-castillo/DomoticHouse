########################################################################
## IMPORTS
########################################################################
import sys, json
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui
from PySide2.QtSerialPort import QSerialPort, QSerialPortInfo

########################################################################
# IMPORT GUI FILE
from ui_DomoticApp import *
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Utils variables for window functions
        self.clickPosition = None
        self.buttonGroupPages = { 
            "livingroom" : [self.ui.livingroomPage, self.ui.livingroomBtn], 
            "office" : [self.ui.officePage, self.ui.officeBtn], 
            "bedroom" : [self.ui.bedroomPage, self.ui.bedroomBtn], 
            "settings" : [self.ui.settingsPage, self.ui.settingsBtn]}
        self.menuCollapsedWidth = 55
        self.menuExpandedWidth = 155

        self.uisingWifi = False

        self.data = {
            "living": 
                {"lights": "off", 
                 "blinds": "down",
                 "air": {"speed": "baja", "state": "off"}}
            }
        
        self.setWindowTitle("Domotic App")
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/window-icon.ico"))

        self.ui.setConectionMethod.clicked.connect(self.changeConnectionMethod)

        #Set left menu buttons functions
        self.ui.menuBtn.clicked.connect(self.toggleMenu)
        self.ui.livingroomBtn.clicked.connect(lambda: 
                                            self.changePage("livingroom"))
        self.ui.officeBtn.clicked.connect(lambda: self.changePage("office"))
        self.ui.bedroomBtn.clicked.connect(lambda: self.changePage("bedroom"))
        self.ui.settingsBtn.clicked.connect(lambda: self.changePage("settings"))


        #Set serial port functions
        self.ui.disconnectBtn.hide()
        self.serial = QSerialPort()
        self.ui.updateBtn.clicked.connect(self.readPorts)
        self.ui.connectBtn.clicked.connect(self.serialConnect)
        self.ui.disconnectBtn.clicked.connect(lambda: self.serialDisconnect())
        self.serial.readyRead.connect(self.serialRead)

        #Set room lights buttons functions and set them checkable
        self.ui.livingLightsBtn.setCheckable(True)
        self.ui.livingLightsBtn.clicked.connect(lambda: self.lights("livingLightsBtn", "living"))

        #Set room blinds buttons functions
        self.ui.livingBlindUpBtn.clicked.connect(lambda: self.blinds
                                                ("living", "up"))
        self.ui.livingBlindDownBtn.clicked.connect(lambda: self.blinds
                                                ("living", "down"))
        
        #Set room air conditioner buttons functions and set them checkable
        self.ui.livingAirBtn.setCheckable(True)
        self.ui.livingAirBtn.clicked.connect(lambda: self.airConditioner
                                                ("livingAirBtn", "living"))
        
        #Set air conditioner speed
        self.ui.livingAirSpeed.currentTextChanged.connect(lambda: 
                                self.setAirSpeed("livingAirSpeed", "living"))
        
        self.show() 

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
            self.ui.setConectionMethod.setText("Cambiar a Serial")
            self.uisingWifi = True

    ########################################################################
    ## Functions refred to comunications
    ########################################################################
    def readPorts(self):
        """
        Reads all available serial ports and add them to the ports combobox
        """
        self.ui.serial_ports_list.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.ui.serial_ports_list.addItem(port.portName())
        self.ui.baudrates_list.setCurrentText("115200")

    def serialConnect(self):
            """
            Connects to the serial port selected in the ports combobox.
            Sets the port name and baudrate, opens the serial port for reading and writing.
            Hides the connect button and shows the disconnect button if the serial port is successfully opened.
            """
            self.serial.waitForReadyRead(500)
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
        print(self.serial.readLine().data().decode().strip())
        #humidTemp = json.loads(humidTemp)

        """self.ui.livingTemperatureLbl.setText(
            self.data["living"]["temperature"] + "ºC")
        self.ui.livingHumidityLbl.setText(
            self.data["living"]["humidity"] + "%")
        
        self.ui.officeTemperatureLbl.setText(
            self.data["office"]["temperature"] + "ºC")
        self.ui.officeTemperatureLbl.setText(
            self.data["office"]["humidity"] + "%")"""
        
    def sendData(self):
        """
        Sends the data to the serial port
        """
        print(self.data)
        json_data = json.dumps(self.data)

        # Abre el puerto serie si está disponible
        if self.serial.isOpen():
            self.serial.write(json_data.encode())
        elif self.uisingWifi:
            # Enviar por wifi
            pass
        else:
            print("No hay conexión")
    
    def wifiRead(self):
        """
        Reads the data from the wifi
        """
        pass

    ########################################################################
    ## Functions refred to rooms 
    ########################################################################
    def lights(self, roomLightBtn, room):
        """
        Sends the command to the serial port to turn on/off the lights and 
        changes the button icon and text
        """
        if not self.serial.isOpen() and not self.uisingWifi: return
        button = getattr(self.ui, roomLightBtn)
        if button.isChecked():
            self.data[room]["lights"] = "on"
            button.setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
            button.setText("On")
        else:
            self.data[room]["lights"] = "off"
            button.setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
            button.setText("Off")
        self.sendData()

    def blinds(self, room, direction):
        if not self.serial.isOpen() and not self.uisingWifi: return
        if self.data[room]["blinds"] == direction: return

        if self.data[room]["blinds"] == "down" and direction == "up":
            self.data[room]["blinds"] = direction
        elif self.data[room]["blinds"] == "up" and direction == "down":
            self.data[room]["blinds"] = direction
        self.sendData()

    def airConditioner(self, roomAirBtn, room):
        if not self.serial.isOpen() and not self.uisingWifi: return
        button = getattr(self.ui, roomAirBtn)
        if button.isChecked():
            self.data[room]["air"]["state"] = "on"
            button.setIcon(QtGui.QIcon(":/icons/icons/toggle-right.svg"))
            button.setText("On")
        else:
            self.data[room]["air"]["state"] = "off"
            button.setIcon(QtGui.QIcon(":/icons/icons/toggle-left.svg"))
            button.setText("Off")
        self.sendData()
    
    def setAirSpeed(self, roomAirOptions, room): 
        if not self.serial.isOpen() and not self.uisingWifi: return
        roomAirOptions = getattr(self.ui, roomAirOptions)
        self.data[room]["air"]["speed"] = roomAirOptions.currentText()
        self.sendData()
        
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
