# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DomoticAppfRjlls.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 391)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #eff3f5;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #192229;\n"
"}\n"
"\n"
"#leftMenuSubcontainer{\n"
"	background-color: #212e36;\n"
"}\n"
"\n"
"#leftMenuSubcontainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#ports, #budrates, #lights, #blinds, #temperature, #airConditioner{\n"
"	background-color: #212e36;\n"
"	border-radius: 10px;\n"
"	border-style: solid;\n"
"	border-width: 4px;\n"
"	border-color: #2a3b47;\n"
"}\n"
"#control_buttons QPushButton{\n"
"	background-color: #52a5e0;\n"
"	border-radius: 15px;\n"
"	padding: 5px 20px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubcontainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubcontainer.setObjectName(u"leftMenuSubcontainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubcontainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubcontainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubcontainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.livingroomBtn = QPushButton(self.frame_2)
        self.livingroomBtn.setObjectName(u"livingroomBtn")
        font = QFont()
        font.setPointSize(12)
        self.livingroomBtn.setFont(font)
        self.livingroomBtn.setStyleSheet(u"background-color: #52a5e0;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/tv.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingroomBtn.setIcon(icon1)
        self.livingroomBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.livingroomBtn)

        self.officeBtn = QPushButton(self.frame_2)
        self.officeBtn.setObjectName(u"officeBtn")
        self.officeBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.officeBtn.setIcon(icon2)
        self.officeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.officeBtn)

        self.bedroomBtn = QPushButton(self.frame_2)
        self.bedroomBtn.setObjectName(u"bedroomBtn")
        self.bedroomBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/bed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bedroomBtn.setIcon(icon3)
        self.bedroomBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.bedroomBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubcontainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.settingsBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubcontainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.headerContainer)
        self.logo.setObjectName(u"logo")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.logo)

        self.botones_ventana = QFrame(self.headerContainer)
        self.botones_ventana.setObjectName(u"botones_ventana")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.botones_ventana.sizePolicy().hasHeightForWidth())
        self.botones_ventana.setSizePolicy(sizePolicy2)
        self.botones_ventana.setFrameShape(QFrame.StyledPanel)
        self.botones_ventana.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.botones_ventana)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.minimizeBtn = QPushButton(self.botones_ventana)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        sizePolicy1.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy1)
        self.minimizeBtn.setMinimumSize(QSize(40, 0))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon5)
        self.minimizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.botones_ventana)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        sizePolicy1.setHeightForWidth(self.maximizeBtn.sizePolicy().hasHeightForWidth())
        self.maximizeBtn.setSizePolicy(sizePolicy1)
        self.maximizeBtn.setMinimumSize(QSize(40, 0))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon6)
        self.maximizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.botones_ventana)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy1.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy1)
        self.closeBtn.setMinimumSize(QSize(40, 0))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon7)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.botones_ventana)


        self.verticalLayout_4.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.mainBodyContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"")
        self.livingroomPage = QWidget()
        self.livingroomPage.setObjectName(u"livingroomPage")
        self.verticalLayout_5 = QVBoxLayout(self.livingroomPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lights_blinds = QWidget(self.livingroomPage)
        self.lights_blinds.setObjectName(u"lights_blinds")
        self.horizontalLayout_9 = QHBoxLayout(self.lights_blinds)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 7)
        self.lights = QFrame(self.lights_blinds)
        self.lights.setObjectName(u"lights")
        self.lights.setFrameShape(QFrame.StyledPanel)
        self.lights.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.lights)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.lights)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_7.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton = QPushButton(self.lights)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/toggle-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.lights)

        self.blinds = QFrame(self.lights_blinds)
        self.blinds.setObjectName(u"blinds")
        self.blinds.setFrameShape(QFrame.StyledPanel)
        self.blinds.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.blinds)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.blinds)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_4 = QFrame(self.blinds)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.livingBlindDownBtn = QPushButton(self.frame_4)
        self.livingBlindDownBtn.setObjectName(u"livingBlindDownBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/chevrons-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingBlindDownBtn.setIcon(icon9)
        self.livingBlindDownBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.livingBlindDownBtn)

        self.livingBlindUpBtn = QPushButton(self.frame_4)
        self.livingBlindUpBtn.setObjectName(u"livingBlindUpBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/chevrons-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingBlindUpBtn.setIcon(icon10)
        self.livingBlindUpBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.livingBlindUpBtn)


        self.verticalLayout_10.addWidget(self.frame_4)


        self.horizontalLayout_9.addWidget(self.blinds)


        self.verticalLayout_5.addWidget(self.lights_blinds)

        self.temp_airConditioner = QWidget(self.livingroomPage)
        self.temp_airConditioner.setObjectName(u"temp_airConditioner")
        self.verticalLayout_9 = QVBoxLayout(self.temp_airConditioner)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.temperature = QFrame(self.temp_airConditioner)
        self.temperature.setObjectName(u"temperature")
        sizePolicy1.setHeightForWidth(self.temperature.sizePolicy().hasHeightForWidth())
        self.temperature.setSizePolicy(sizePolicy1)
        self.temperature.setFrameShape(QFrame.StyledPanel)
        self.temperature.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.temperature)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.temperature)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temperaturerLbl = QLabel(self.temperature)
        self.temperaturerLbl.setObjectName(u"temperaturerLbl")
        self.temperaturerLbl.setFont(font2)

        self.horizontalLayout_11.addWidget(self.temperaturerLbl, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.temperature)

        self.airConditioner = QFrame(self.temp_airConditioner)
        self.airConditioner.setObjectName(u"airConditioner")
        self.airConditioner.setFrameShape(QFrame.StyledPanel)
        self.airConditioner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.airConditioner)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.airConditioner)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_5 = QFrame(self.airConditioner)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.airConditionerBtn = QPushButton(self.frame_5)
        self.airConditionerBtn.setObjectName(u"airConditionerBtn")
        self.airConditionerBtn.setFont(font2)
        self.airConditionerBtn.setIcon(icon8)
        self.airConditionerBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.airConditionerBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_9, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.airConditionerSpeed = QComboBox(self.frame_5)
        self.airConditionerSpeed.setObjectName(u"airConditionerSpeed")
        self.airConditionerSpeed.setFont(font2)
        self.airConditionerSpeed.setEditable(False)

        self.horizontalLayout_12.addWidget(self.airConditionerSpeed, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.frame_5)


        self.verticalLayout_9.addWidget(self.airConditioner)


        self.verticalLayout_5.addWidget(self.temp_airConditioner)

        self.stackedWidget.addWidget(self.livingroomPage)
        self.officePage = QWidget()
        self.officePage.setObjectName(u"officePage")
        self.verticalLayout_6 = QVBoxLayout(self.officePage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.officePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.officePage)
        self.bedroomPage = QWidget()
        self.bedroomPage.setObjectName(u"bedroomPage")
        self.verticalLayout_7 = QVBoxLayout(self.bedroomPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.bedroomPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.bedroomPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_8 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.ports = QFrame(self.settingsPage)
        self.ports.setObjectName(u"ports")
        self.ports.setStyleSheet(u"")
        self.ports.setFrameShape(QFrame.StyledPanel)
        self.ports.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ports)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.ports)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.serial_ports_list = QComboBox(self.ports)
        self.serial_ports_list.setObjectName(u"serial_ports_list")
        sizePolicy1.setHeightForWidth(self.serial_ports_list.sizePolicy().hasHeightForWidth())
        self.serial_ports_list.setSizePolicy(sizePolicy1)
        self.serial_ports_list.setFont(font2)

        self.horizontalLayout_3.addWidget(self.serial_ports_list, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.ports, 0, Qt.AlignVCenter)

        self.budrates = QFrame(self.settingsPage)
        self.budrates.setObjectName(u"budrates")
        sizePolicy3.setHeightForWidth(self.budrates.sizePolicy().hasHeightForWidth())
        self.budrates.setSizePolicy(sizePolicy3)
        self.budrates.setFrameShape(QFrame.StyledPanel)
        self.budrates.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.budrates)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.budrates)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.baudrates_list = QComboBox(self.budrates)
        self.baudrates_list.setObjectName(u"baudrates_list")
        self.baudrates_list.setFont(font2)

        self.horizontalLayout_5.addWidget(self.baudrates_list, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.budrates, 0, Qt.AlignVCenter)

        self.control_buttons = QFrame(self.settingsPage)
        self.control_buttons.setObjectName(u"control_buttons")
        self.control_buttons.setFrameShape(QFrame.StyledPanel)
        self.control_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.control_buttons)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.updateBtn = QPushButton(self.control_buttons)
        self.updateBtn.setObjectName(u"updateBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.updateBtn.sizePolicy().hasHeightForWidth())
        self.updateBtn.setSizePolicy(sizePolicy4)
        self.updateBtn.setFont(font1)

        self.horizontalLayout_6.addWidget(self.updateBtn)

        self.connectBtn = QPushButton(self.control_buttons)
        self.connectBtn.setObjectName(u"connectBtn")
        sizePolicy4.setHeightForWidth(self.connectBtn.sizePolicy().hasHeightForWidth())
        self.connectBtn.setSizePolicy(sizePolicy4)
        self.connectBtn.setFont(font1)

        self.horizontalLayout_6.addWidget(self.connectBtn)

        self.disconnectBtn = QPushButton(self.control_buttons)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        sizePolicy4.setHeightForWidth(self.disconnectBtn.sizePolicy().hasHeightForWidth())
        self.disconnectBtn.setSizePolicy(sizePolicy4)
        self.disconnectBtn.setFont(font1)

        self.horizontalLayout_6.addWidget(self.disconnectBtn)


        self.verticalLayout_8.addWidget(self.control_buttons, 0, Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.settingsPage)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.livingroomBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Livingroom", None))
#endif // QT_CONFIG(tooltip)
        self.livingroomBtn.setText(QCoreApplication.translate("MainWindow", u"Sal\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.officeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Office", None))
#endif // QT_CONFIG(tooltip)
        self.officeBtn.setText(QCoreApplication.translate("MainWindow", u"Oficina", None))
#if QT_CONFIG(tooltip)
        self.bedroomBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Bedroom", None))
#endif // QT_CONFIG(tooltip)
        self.bedroomBtn.setText(QCoreApplication.translate("MainWindow", u"Dormitorio", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Luces", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Persianas", None))
        self.livingBlindDownBtn.setText("")
        self.livingBlindUpBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.temperaturerLbl.setText(QCoreApplication.translate("MainWindow", u"30\u00baC", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Aire Acondicionado", None))
        self.airConditionerBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" Velocidad", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Oficina", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dormitorio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Serial Port", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Baudrate", None))
        self.updateBtn.setText(QCoreApplication.translate("MainWindow", u"Actualizar Puertos", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Conectar ", None))
        self.disconnectBtn.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
    # retranslateUi

