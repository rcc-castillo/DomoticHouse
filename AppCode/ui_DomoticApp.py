# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DomoticApprhjEOB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 483)
        MainWindow.setMinimumSize(QSize(365, 0))
        MainWindow.setMaximumSize(QSize(700, 16777215))
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
"#ports, #budrates, #livingLights, #livingBlinds, #livingHumidTemp, #livingAir, #officeLights, #officeBlinds, #officeHumidTemp, #officeAir, #gardenIrrigation{\n"
"	background-color: #212e36;\n"
"	border-radius: 10px;\n"
"	border-style: solid;\n"
"	border-width: 2.5px;\n"
"	border-color: #2a3b47;\n"
"}\n"
"\n"
"#footerContainer{\n"
"	background-color: #212e36;\n"
"	border-radius: 10px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #2a3b47;\n"
"}\n"
"\n"
"#settingsPage QPushButton{\n"
"	background-color: #52a5e0;\n"
"	border-radius: 15px;"
                        "\n"
"	padding: 5px 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	background-color: #2a3b47;\n"
"	selection-background-color: #52a5e0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        self.logo = QLabel(self.headerContainer)
        self.logo.setObjectName(u"logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy2)
        self.logo.setMinimumSize(QSize(270, 50))
        self.logo.setMaximumSize(QSize(270, 50))
        self.logo.setPixmap(QPixmap(u":/icons/icons/app-icon.svg"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.logo, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainPages = QStackedWidget(self.mainBodyContainer)
        self.mainPages.setObjectName(u"mainPages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainPages.sizePolicy().hasHeightForWidth())
        self.mainPages.setSizePolicy(sizePolicy3)
        self.mainPages.setStyleSheet(u"")
        self.livingroomPage = QWidget()
        self.livingroomPage.setObjectName(u"livingroomPage")
        self.verticalLayout_5 = QVBoxLayout(self.livingroomPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_6 = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.livingWidgets = QGridLayout()
        self.livingWidgets.setObjectName(u"livingWidgets")
        self.livingWidgets.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.livingBlinds = QWidget(self.livingroomPage)
        self.livingBlinds.setObjectName(u"livingBlinds")
        self.verticalLayout_15 = QVBoxLayout(self.livingBlinds)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.livingBlinds)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)

        self.verticalLayout_15.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_11 = QFrame(self.livingBlinds)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.livingRoomBlindsDownBtn = QPushButton(self.frame_11)
        self.livingRoomBlindsDownBtn.setObjectName(u"livingRoomBlindsDownBtn")
        self.livingRoomBlindsDownBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/chevrons-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingRoomBlindsDownBtn.setIcon(icon)
        self.livingRoomBlindsDownBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.livingRoomBlindsDownBtn)

        self.livingRoomBlindsUpBtn = QPushButton(self.frame_11)
        self.livingRoomBlindsUpBtn.setObjectName(u"livingRoomBlindsUpBtn")
        self.livingRoomBlindsUpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/chevrons-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingRoomBlindsUpBtn.setIcon(icon1)
        self.livingRoomBlindsUpBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.livingRoomBlindsUpBtn)


        self.verticalLayout_15.addWidget(self.frame_11)


        self.livingWidgets.addWidget(self.livingBlinds, 0, 1, 1, 1)

        self.livingLights = QWidget(self.livingroomPage)
        self.livingLights.setObjectName(u"livingLights")
        self.verticalLayout_11 = QVBoxLayout(self.livingLights)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.livingLights)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_11.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.livingRoomLightsBtn = QPushButton(self.livingLights)
        self.livingRoomLightsBtn.setObjectName(u"livingRoomLightsBtn")
        sizePolicy1.setHeightForWidth(self.livingRoomLightsBtn.sizePolicy().hasHeightForWidth())
        self.livingRoomLightsBtn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.livingRoomLightsBtn.setFont(font1)
        self.livingRoomLightsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/toggle-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingRoomLightsBtn.setIcon(icon2)
        self.livingRoomLightsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.livingRoomLightsBtn)


        self.livingWidgets.addWidget(self.livingLights, 0, 0, 1, 1)

        self.livingAir = QWidget(self.livingroomPage)
        self.livingAir.setObjectName(u"livingAir")
        self.verticalLayout_16 = QVBoxLayout(self.livingAir)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_15 = QLabel(self.livingAir)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_16.addWidget(self.label_15, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.livingAirOptions = QFrame(self.livingAir)
        self.livingAirOptions.setObjectName(u"livingAirOptions")
        self.livingAirOptions.setFrameShape(QFrame.StyledPanel)
        self.livingAirOptions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.livingAirOptions)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.livingRoomAirBtn = QPushButton(self.livingAirOptions)
        self.livingRoomAirBtn.setObjectName(u"livingRoomAirBtn")
        self.livingRoomAirBtn.setFont(font1)
        self.livingRoomAirBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.livingRoomAirBtn.setIcon(icon2)
        self.livingRoomAirBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.livingRoomAirBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_16 = QLabel(self.livingAirOptions)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_16, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.livingRoomAirSpeed = QComboBox(self.livingAirOptions)
        self.livingRoomAirSpeed.addItem("")
        self.livingRoomAirSpeed.addItem("")
        self.livingRoomAirSpeed.addItem("")
        self.livingRoomAirSpeed.setObjectName(u"livingRoomAirSpeed")
        self.livingRoomAirSpeed.setFont(font1)
        self.livingRoomAirSpeed.setEditable(False)

        self.horizontalLayout_15.addWidget(self.livingRoomAirSpeed, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_16.addWidget(self.livingAirOptions)


        self.livingWidgets.addWidget(self.livingAir, 2, 0, 1, 2)

        self.livingHumidTemp = QWidget(self.livingroomPage)
        self.livingHumidTemp.setObjectName(u"livingHumidTemp")
        self.verticalLayout_12 = QVBoxLayout(self.livingHumidTemp)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.livingTemp = QFrame(self.livingHumidTemp)
        self.livingTemp.setObjectName(u"livingTemp")
        self.livingTemp.setFrameShape(QFrame.StyledPanel)
        self.livingTemp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.livingTemp)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.livingTemp)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.livingRoomHumidtempTemperatureLbl = QLabel(self.livingTemp)
        self.livingRoomHumidtempTemperatureLbl.setObjectName(u"livingRoomHumidtempTemperatureLbl")
        self.livingRoomHumidtempTemperatureLbl.setFont(font1)

        self.horizontalLayout_11.addWidget(self.livingRoomHumidtempTemperatureLbl, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.livingTemp)

        self.livingHumid = QFrame(self.livingHumidTemp)
        self.livingHumid.setObjectName(u"livingHumid")
        self.livingHumid.setFrameShape(QFrame.StyledPanel)
        self.livingHumid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.livingHumid)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_17 = QLabel(self.livingHumid)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.livingRoomHumidtempHumidityLbl = QLabel(self.livingHumid)
        self.livingRoomHumidtempHumidityLbl.setObjectName(u"livingRoomHumidtempHumidityLbl")
        self.livingRoomHumidtempHumidityLbl.setFont(font1)

        self.horizontalLayout_10.addWidget(self.livingRoomHumidtempHumidityLbl, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.livingHumid)


        self.livingWidgets.addWidget(self.livingHumidTemp, 1, 0, 1, 2)


        self.verticalLayout_5.addLayout(self.livingWidgets)

        self.verticalSpacer_7 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.mainPages.addWidget(self.livingroomPage)
        self.gardenPage = QWidget()
        self.gardenPage.setObjectName(u"gardenPage")
        self.verticalLayout_22 = QVBoxLayout(self.gardenPage)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)

        self.gardenWidgets = QGridLayout()
        self.gardenWidgets.setObjectName(u"gardenWidgets")
        self.gardenWidgets.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gardenIrrigation = QWidget(self.gardenPage)
        self.gardenIrrigation.setObjectName(u"gardenIrrigation")
        self.verticalLayout_7 = QVBoxLayout(self.gardenIrrigation)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.gardenIrrigation)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.irrigationOptions = QFrame(self.gardenIrrigation)
        self.irrigationOptions.setObjectName(u"irrigationOptions")
        self.irrigationOptions.setFrameShape(QFrame.StyledPanel)
        self.irrigationOptions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.irrigationOptions)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gardenIrrigationBtn = QPushButton(self.irrigationOptions)
        self.gardenIrrigationBtn.setObjectName(u"gardenIrrigationBtn")
        sizePolicy1.setHeightForWidth(self.gardenIrrigationBtn.sizePolicy().hasHeightForWidth())
        self.gardenIrrigationBtn.setSizePolicy(sizePolicy1)
        self.gardenIrrigationBtn.setFont(font1)
        self.gardenIrrigationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.gardenIrrigationBtn.setIcon(icon2)
        self.gardenIrrigationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.gardenIrrigationBtn)

        self.irrigationSelectors = QFrame(self.irrigationOptions)
        self.irrigationSelectors.setObjectName(u"irrigationSelectors")
        self.irrigationSelectors.setFrameShape(QFrame.StyledPanel)
        self.irrigationSelectors.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.irrigationSelectors)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_5 = QFrame(self.irrigationSelectors)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_8)

        self.gardenIrrigationStartTime = QTimeEdit(self.frame_5)
        self.gardenIrrigationStartTime.setObjectName(u"gardenIrrigationStartTime")
        self.gardenIrrigationStartTime.setFont(font1)

        self.horizontalLayout_17.addWidget(self.gardenIrrigationStartTime)


        self.verticalLayout_19.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.irrigationSelectors)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_9)

        self.gardenIrrigationEndTime = QTimeEdit(self.frame_6)
        self.gardenIrrigationEndTime.setObjectName(u"gardenIrrigationEndTime")
        self.gardenIrrigationEndTime.setFont(font1)

        self.horizontalLayout_18.addWidget(self.gardenIrrigationEndTime)


        self.verticalLayout_19.addWidget(self.frame_6)


        self.horizontalLayout_8.addWidget(self.irrigationSelectors)


        self.verticalLayout_7.addWidget(self.irrigationOptions)


        self.gardenWidgets.addWidget(self.gardenIrrigation, 0, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gardenWidgets)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_8)

        self.mainPages.addWidget(self.gardenPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_8 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.serialPortConection = QFrame(self.settingsPage)
        self.serialPortConection.setObjectName(u"serialPortConection")
        self.serialPortConection.setFrameShape(QFrame.StyledPanel)
        self.serialPortConection.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.serialPortConection)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ports = QFrame(self.serialPortConection)
        self.ports.setObjectName(u"ports")
        self.ports.setStyleSheet(u"")
        self.ports.setFrameShape(QFrame.StyledPanel)
        self.ports.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ports)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.ports)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.serial_ports_list = QComboBox(self.ports)
        self.serial_ports_list.setObjectName(u"serial_ports_list")
        sizePolicy1.setHeightForWidth(self.serial_ports_list.sizePolicy().hasHeightForWidth())
        self.serial_ports_list.setSizePolicy(sizePolicy1)
        self.serial_ports_list.setFont(font1)
        self.serial_ports_list.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.serial_ports_list, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.ports)

        self.budrates = QFrame(self.serialPortConection)
        self.budrates.setObjectName(u"budrates")
        sizePolicy3.setHeightForWidth(self.budrates.sizePolicy().hasHeightForWidth())
        self.budrates.setSizePolicy(sizePolicy3)
        self.budrates.setFrameShape(QFrame.StyledPanel)
        self.budrates.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.budrates)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.budrates)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.baudrates_list = QComboBox(self.budrates)
        self.baudrates_list.addItem("")
        self.baudrates_list.addItem("")
        self.baudrates_list.addItem("")
        self.baudrates_list.addItem("")
        self.baudrates_list.addItem("")
        self.baudrates_list.addItem("")
        self.baudrates_list.addItem("")
        self.baudrates_list.setObjectName(u"baudrates_list")
        self.baudrates_list.setFont(font1)
        self.baudrates_list.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.baudrates_list, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.budrates)

        self.control_buttons = QFrame(self.serialPortConection)
        self.control_buttons.setObjectName(u"control_buttons")
        self.control_buttons.setFrameShape(QFrame.StyledPanel)
        self.control_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.control_buttons)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.updateBtn = QPushButton(self.control_buttons)
        self.updateBtn.setObjectName(u"updateBtn")
        sizePolicy2.setHeightForWidth(self.updateBtn.sizePolicy().hasHeightForWidth())
        self.updateBtn.setSizePolicy(sizePolicy2)
        self.updateBtn.setFont(font)
        self.updateBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.updateBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.connectBtn = QPushButton(self.control_buttons)
        self.connectBtn.setObjectName(u"connectBtn")
        sizePolicy2.setHeightForWidth(self.connectBtn.sizePolicy().hasHeightForWidth())
        self.connectBtn.setSizePolicy(sizePolicy2)
        self.connectBtn.setFont(font)
        self.connectBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.connectBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.disconnectBtn = QPushButton(self.control_buttons)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        sizePolicy2.setHeightForWidth(self.disconnectBtn.sizePolicy().hasHeightForWidth())
        self.disconnectBtn.setSizePolicy(sizePolicy2)
        self.disconnectBtn.setFont(font)
        self.disconnectBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.disconnectBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.control_buttons)


        self.verticalLayout_8.addWidget(self.serialPortConection)

        self.setConectionMethod = QPushButton(self.settingsPage)
        self.setConectionMethod.setObjectName(u"setConectionMethod")
        sizePolicy2.setHeightForWidth(self.setConectionMethod.sizePolicy().hasHeightForWidth())
        self.setConectionMethod.setSizePolicy(sizePolicy2)
        self.setConectionMethod.setFont(font)
        self.setConectionMethod.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.setConectionMethod, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.mainPages.addWidget(self.settingsPage)

        self.verticalLayout_4.addWidget(self.mainPages)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.verticalLayout_6 = QVBoxLayout(self.footerContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.notification = QLabel(self.footerContainer)
        self.notification.setObjectName(u"notification")
        self.notification.setFont(font1)

        self.verticalLayout_6.addWidget(self.notification, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.footerContainer, 0, Qt.AlignVCenter)


        self.gridLayout.addWidget(self.mainBodyContainer, 0, 1, 1, 1)

        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(55, 16777215))
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
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon3)
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
        font2 = QFont()
        font2.setPointSize(12)
        self.livingroomBtn.setFont(font2)
        self.livingroomBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.livingroomBtn.setStyleSheet(u"background-color: #52a5e0;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/tv.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingroomBtn.setIcon(icon4)
        self.livingroomBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.livingroomBtn)

        self.gardenBtn = QPushButton(self.frame_2)
        self.gardenBtn.setObjectName(u"gardenBtn")
        self.gardenBtn.setFont(font2)
        self.gardenBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/garden.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gardenBtn.setIcon(icon5)
        self.gardenBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.gardenBtn)


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
        self.settingsBtn.setFont(font2)
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.settingsBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubcontainer, 0, Qt.AlignLeft)


        self.gridLayout.addWidget(self.leftMenuContainer, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Persianas", None))
        self.livingRoomBlindsDownBtn.setText("")
        self.livingRoomBlindsUpBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Luces", None))
        self.livingRoomLightsBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Aire Acondicionado", None))
        self.livingRoomAirBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u" Velocidad", None))
        self.livingRoomAirSpeed.setItemText(0, QCoreApplication.translate("MainWindow", u"Baja", None))
        self.livingRoomAirSpeed.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))
        self.livingRoomAirSpeed.setItemText(2, QCoreApplication.translate("MainWindow", u"Alta", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.livingRoomHumidtempTemperatureLbl.setText(QCoreApplication.translate("MainWindow", u"30\u00baC", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Humedad", None))
        self.livingRoomHumidtempHumidityLbl.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Riego Autom\u00e1tico", None))
        self.gardenIrrigationBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hora de inicio: ", None))
        self.gardenIrrigationStartTime.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Hora de apagado: ", None))
        self.gardenIrrigationEndTime.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Serial Port", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Baudrate", None))
        self.baudrates_list.setItemText(0, QCoreApplication.translate("MainWindow", u"1200", None))
        self.baudrates_list.setItemText(1, QCoreApplication.translate("MainWindow", u"2400", None))
        self.baudrates_list.setItemText(2, QCoreApplication.translate("MainWindow", u"4800", None))
        self.baudrates_list.setItemText(3, QCoreApplication.translate("MainWindow", u"9600", None))
        self.baudrates_list.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.baudrates_list.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.baudrates_list.setItemText(6, QCoreApplication.translate("MainWindow", u"115200", None))

        self.updateBtn.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Conectar ", None))
        self.disconnectBtn.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.setConectionMethod.setText(QCoreApplication.translate("MainWindow", u"Cambiar a Wifi", None))
        self.notification.setText("")
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.livingroomBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Livingroom", None))
#endif // QT_CONFIG(tooltip)
        self.livingroomBtn.setText(QCoreApplication.translate("MainWindow", u"Sal\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.gardenBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Show Jard\u00edn</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gardenBtn.setText(QCoreApplication.translate("MainWindow", u"Jard\u00edn", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
    # retranslateUi

