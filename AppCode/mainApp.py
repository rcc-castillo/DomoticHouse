########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui

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

        

        self.show() 


    #Functions refred to GUI functions
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
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
