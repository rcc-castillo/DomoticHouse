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
from Wifi import Wifi
from SerialConnection import SerialConnection
from RoomController import RoomController
from CommunicationController import CommunicationController
from RoomUiController import RoomUiController
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.communicationController = CommunicationController()
        self.roomUiController = RoomUiController(self.ui)
        self.roomController = RoomController(self.roomUiController, self.communicationController)

        self.dataTimer = QTimer() 
        self.dataTimer.timeout.connect(self.updateHumidityTemperature)

        self.roomsTimer = QTimer()
        self.roomsTimer.start(200)
        self.roomsTimer.timeout.connect(self.updateRooms)

        self.show()
    
    def initUI(self):
        self.setWindowTitle("Domotic App")
        self.setWindowIcon(QIcon(":/icons/icons/window-icon.ico"))
        self.changePage("settings")
        self.ui.footerContainer.hide()
        
        #Set connection method button function
        self.ui.setConectionMethod.clicked.connect(self.togleConectionMethod)
        
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
        pageUi = getattr(self.ui, f"{pageName}Page")
        self.ui.mainPages.setCurrentWidget(pageUi)
        for button in ["livingroom", "garden", "settings"]:
            style = u"background-color: #52a5e0;" if button == pageName else u"background-color: transparent;"
            buttonUi = getattr(self.ui, f"{button}Btn")
            buttonUi.setStyleSheet(style)
    
    def updatePorts(self):
        self.ui.serial_ports_list.clear()
        self.ui.serial_ports_list.addItems(self.communicationController.getSerialPorts())
        self.ui.baudrates_list.setCurrentText("9600")
    
    def serialConnect(self):
        self.communicationController.serialConnect(self.ui.serial_ports_list.currentText(), 9600)
        if not self.communicationController.serialIsConnected: return
        self.ui.connectBtn.hide()
        self.ui.disconnectBtn.show()
    
    def serialDisconnect(self):
        self.communicationController.serialDisconnect()
        self.ui.connectBtn.show()
        self.ui.disconnectBtn.hide()
    
    def togleConectionMethod(self):
        self.communicationController.toggleConnectionMethod()
        self.ui.serialPortConection.setVisible(not self.communicationController.wifiIsConnected())
        if not self.communicationController.wifiIsConnected():
            self.ui.setConectionMethod.setText("Cambiar a Wifi")
        elif not self.communicationController.serialIsConnected():
            self.ui.setConectionMethod.setText("Cambiar a Serial")
    
    def updateRooms(self):
        data = self.communicationController.getRooms()
        if data is None: return
        self.roomController.updateRooms(data)
        self.roomsTimer.stop()
        self.notification("Habitaciones actualizadas")
        self.roomController.initRoomButtons()
        if self.communicationController.serialIsConnected():
            self.communicationController.serialClear()
        self.dataTimer.start(1000)

    def updateHumidityTemperature(self):
        data = self.communicationController.getData()
        if data is None: return
        self.roomController.updateHumidityTemperature(data)
        
    def notification(self, message):
        self.ui.notification.setText(message)
        self.ui.footerContainer.show()
        QTimer.singleShot(3000, lambda: self.ui.footerContainer.hide())
    
    
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
