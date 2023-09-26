########################################################################
## IMPORTS
########################################################################
import sys
import os
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

        self.data = {
            "living": 
                {"temperature": "0", 
                 "humidity": "0", 
                 "lights": "off", 
                 "blinds": "down",
                 "air": {"speed": "baja", "state": "off"}},
            "office": 
                {"temperature": "0", 
                 "humidity": "0", 
                 "lights": "off", 
                 "blinds": "down",
                 "air": {"speed": "baja", "state": "off"}}}

        #Delete window frame and set size grip to resize window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        QSizeGrip(getattr(self.ui, "size_grip"))

        #Set window title bar buttons
        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.closeBtn.clicked.connect(lambda: self.close())
        self.ui.maximizeBtn.clicked.connect(lambda: 
                                            self.restore_or_maximize_window())
        
        #Set window title bar functions to move window and toggle window size
        self.ui.headerContainer.mouseMoveEvent = self.moveWindow
        self.ui.headerContainer.mouseDoubleClickEvent = self.toggleWindowSize

        #Set left menu buttons functions
        self.ui.menuBtn.clicked.connect(self.toggleMenu)
        self.ui.livingroomBtn.clicked.connect(lambda: 
                                            self.changePage("livingroom"))
        self.ui.officeBtn.clicked.connect(lambda: self.changePage("office"))
        self.ui.bedroomBtn.clicked.connect(lambda: self.changePage("bedroom"))
        self.ui.settingsBtn.clicked.connect(lambda: self.changePage("settings"))


        #Set serial port functions
        self.serial = QSerialPort()
        self.ui.updateBtn.clicked.connect(self.readPorts)
        self.ui.connectBtn.clicked.connect(self.serialConnect)
        self.ui.disconnectBtn.clicked.connect(lambda: self.serial.close())
        self.serial.readyRead.connect(self.serialRead)

        #Set room lights buttons functions and set them checkable
        self.ui.livingLightsBtn.setCheckable(True)
        self.ui.officeLightsBtn.setCheckable(True)
        self.ui.livingLightsBtn.clicked.connect(lambda: self.lights("livingLightsBtn", "living"))
        self.ui.officeLightsBtn.clicked.connect(lambda: self.lights("officeLightsBtn", "office"))

        #Set room blinds buttons functions
        self.ui.livingBlindUpBtn.clicked.connect(lambda: self.blinds
                                                ("living", "up"))
        self.ui.livingBlindDownBtn.clicked.connect(lambda: self.blinds
                                                ("living", "down"))
        self.ui.officeBlindUpBtn.clicked.connect(lambda: self.blinds
                                                ("office", "up"))
        self.ui.officeBlindDownBtn.clicked.connect(lambda: self.blinds
                                                ("office", "down"))
        
        #Set room air conditioner buttons functions and set them checkable
        self.ui.livingAirBtn.setCheckable(True)
        self.ui.officeAirBtn.setCheckable(True)
        self.ui.livingAirBtn.clicked.connect(lambda: self.airConditioner
                                                ("livingAirBtn", "living"))
        self.ui.officeAirBtn.clicked.connect(lambda: self.airConditioner
                                                ("officeAirBtn", "office"))
        
        #Set air conditioner speed
        self.ui.livingAirSpeed.currentTextChanged.connect(lambda: 
                                self.setAirSpeed("livingAirSpeed", "living"))
        self.ui.officeAirSpeed.currentTextChanged.connect(lambda: 
                                self.setAirSpeed("officeAirSpeed", "office"))
        
        

        self.show() 

    ########################################################################
    ## Functions refred to GUI functions
    ########################################################################
    def mousePressEvent(self, event):
        """
        Handle mouse press events for the main application window.

        :param event: The mouse press event.
        """
        self.clickPosition = event.globalPos()
        cursor = QtGui.QCursor()
        xPos = cursor.pos().x()
        yPos = cursor.pos().y()
        if hasattr(self, "floatingWidgets"):
            for x in self.floatingWidgets:
                if hasattr(x, "autoHide") and x.autoHide:
                    x.collapseMenu()

    def moveWindow(self, e):
            """
            Moves the window when the left mouse button is clicked and dragged.

            Args:
                e (QMouseEvent): The mouse event that triggered the method.
            """
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    if self.clickPosition is not None:
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                        self.clickPosition = e.globalPos()
                        e.accept()
            else:
                self.showNormal()
    
    def toggleWindowSize(self, e):
            """
            Toggles the size of the window between maximized and normal.

            :param e: The event that triggered the method.
            """
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

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
    
    def restore_or_maximize_window(self):
            """
            Restores or maximizes the window depending on its current state.
            """
            if self.isMaximized():
                self.showNormal()
                self.ui.maximizeBtn.setIcon(QtGui.QIcon(":/icons/icons/square.svg"))
                   
            else:
                self.showMaximized()
                self.ui.maximizeBtn.setIcon(QtGui.QIcon(":/icons/icons/copy.svg"))

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
    ## Functions refred to serial port
    ########################################################################
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
        Connects to the serial port selected in the ports combobox
        """
        self.serial.waitForReadyRead(200)
        port = self.ui.serial_ports_list.currentText()
        baudrate = int(self.ui.baudrates_list.currentText())
        self.serial.setPortName(port)
        self.serial.setBaudRate(baudrate)
        self.serial.open(QSerialPort.ReadWrite)

    def serialRead(self):
        """
        Reads the serial port and returns the data
        """
        if not self.serial.isOpen() or not self.serial.canReadLine(): return
        self.data = self.serial.readLine().data().decode().strip()

        self.ui.livingTemperatureLbl.setText(
            self.data["living"]["temperature"] + "ºC")
        self.ui.livingHumidityLbl.setText(
            self.data["living"]["humidity"] + "%")
        
        self.ui.officeTemperatureLbl.setText(
            self.data["office"]["temperature"] + "ºC")
        self.ui.officeTemperatureLbl.setText(
            self.data["office"]["humidity"] + "%")
        
    def sendData(self):
        """
        Sends the data to the serial port
        """
        print(self.data)
        #transform data to json and send it to serial port
        

    ########################################################################
    ## Functions refred to rooms 
    ########################################################################
    def lights(self, roomLightBtn, room):
        """
        Sends the command to the serial port to turn on/off the lights and 
        changes the button icon and text
        """
        if not self.serial.isOpen(): return
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
        if not self.serial.isOpen(): return
        if self.data[room]["blinds"] == direction: return

        if self.data[room]["blinds"] == "down" and direction == "up":
            self.data[room]["blinds"] = direction
        elif self.data[room]["blinds"] == "up" and direction == "down":
            self.data[room]["blinds"] = direction
        self.sendData()

    def airConditioner(self, roomAirBtn, room):
        #if not self.serial.isOpen(): return
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
        if not self.serial.isOpen(): return
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
