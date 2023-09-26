# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DomoticApptdspGj.ui'
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
        MainWindow.resize(605, 525)
        MainWindow.setMinimumSize(QSize(360, 0))
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
"#ports, #budrates, #livingLights, #livingBlinds, #livingTemperature, #livingAir, #officeLights, #officeBlinds, #officeTemperature, #officeAir{\n"
"	background-color: #212e36;\n"
"	border-radius: 10px;\n"
"	border-style: solid;\n"
"	border-width: 2.5px;\n"
"	border-color: #2a3b47;\n"
"}\n"
"#control_buttons QPushButton{\n"
"	background-color: #52a5e0;\n"
"	border-radius: 15px;\n"
"	padding: 5px 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	background-color: #2a3b47;\n"
" \n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.botones_ventana)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        sizePolicy1.setHeightForWidth(self.maximizeBtn.sizePolicy().hasHeightForWidth())
        self.maximizeBtn.setSizePolicy(sizePolicy1)
        self.maximizeBtn.setMinimumSize(QSize(40, 0))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon1)
        self.maximizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.botones_ventana)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy1.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy1)
        self.closeBtn.setMinimumSize(QSize(40, 0))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.botones_ventana)


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
        self.livingBlindDownBtn = QPushButton(self.frame_11)
        self.livingBlindDownBtn.setObjectName(u"livingBlindDownBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chevrons-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingBlindDownBtn.setIcon(icon3)
        self.livingBlindDownBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.livingBlindDownBtn)

        self.livingBlindUpBtn = QPushButton(self.frame_11)
        self.livingBlindUpBtn.setObjectName(u"livingBlindUpBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/chevrons-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingBlindUpBtn.setIcon(icon4)
        self.livingBlindUpBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.livingBlindUpBtn)


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

        self.livingLightsBtn = QPushButton(self.livingLights)
        self.livingLightsBtn.setObjectName(u"livingLightsBtn")
        sizePolicy1.setHeightForWidth(self.livingLightsBtn.sizePolicy().hasHeightForWidth())
        self.livingLightsBtn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.livingLightsBtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/toggle-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingLightsBtn.setIcon(icon5)
        self.livingLightsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.livingLightsBtn)


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
        self.livingAirBtn = QPushButton(self.livingAirOptions)
        self.livingAirBtn.setObjectName(u"livingAirBtn")
        self.livingAirBtn.setFont(font1)
        self.livingAirBtn.setIcon(icon5)
        self.livingAirBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.livingAirBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_16 = QLabel(self.livingAirOptions)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_16, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.livingAirSpeed = QComboBox(self.livingAirOptions)
        self.livingAirSpeed.addItem("")
        self.livingAirSpeed.addItem("")
        self.livingAirSpeed.addItem("")
        self.livingAirSpeed.setObjectName(u"livingAirSpeed")
        self.livingAirSpeed.setFont(font1)
        self.livingAirSpeed.setEditable(False)

        self.horizontalLayout_15.addWidget(self.livingAirSpeed, 0, Qt.AlignHCenter|Qt.AlignVCenter)


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

        self.horizontalLayout_11.addWidget(self.label_18)

        self.livingTemperatureLbl = QLabel(self.livingTemp)
        self.livingTemperatureLbl.setObjectName(u"livingTemperatureLbl")
        self.livingTemperatureLbl.setFont(font1)

        self.horizontalLayout_11.addWidget(self.livingTemperatureLbl)


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

        self.horizontalLayout_10.addWidget(self.label_17)

        self.livingHumidityLbl = QLabel(self.livingHumid)
        self.livingHumidityLbl.setObjectName(u"livingHumidityLbl")
        self.livingHumidityLbl.setFont(font1)

        self.horizontalLayout_10.addWidget(self.livingHumidityLbl)


        self.verticalLayout_12.addWidget(self.livingHumid)


        self.livingWidgets.addWidget(self.livingHumidTemp, 1, 0, 1, 2)


        self.verticalLayout_5.addLayout(self.livingWidgets)

        self.verticalSpacer_7 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.mainPages.addWidget(self.livingroomPage)
        self.officePage = QWidget()
        self.officePage.setObjectName(u"officePage")
        self.verticalLayout_10 = QVBoxLayout(self.officePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.officeWidgets = QGridLayout()
        self.officeWidgets.setObjectName(u"officeWidgets")
        self.officeWidgets.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.officeLights = QWidget(self.officePage)
        self.officeLights.setObjectName(u"officeLights")
        self.verticalLayout_6 = QVBoxLayout(self.officeLights)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.officeLights)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.officeLightsBtn = QPushButton(self.officeLights)
        self.officeLightsBtn.setObjectName(u"officeLightsBtn")
        sizePolicy1.setHeightForWidth(self.officeLightsBtn.sizePolicy().hasHeightForWidth())
        self.officeLightsBtn.setSizePolicy(sizePolicy1)
        self.officeLightsBtn.setFont(font1)
        self.officeLightsBtn.setIcon(icon5)
        self.officeLightsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.officeLightsBtn)


        self.officeWidgets.addWidget(self.officeLights, 0, 0, 1, 1)

        self.officeBlinds = QWidget(self.officePage)
        self.officeBlinds.setObjectName(u"officeBlinds")
        self.verticalLayout_13 = QVBoxLayout(self.officeBlinds)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.officeBlinds)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_13.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_10 = QFrame(self.officeBlinds)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.officeBlindDownBtn = QPushButton(self.frame_10)
        self.officeBlindDownBtn.setObjectName(u"officeBlindDownBtn")
        self.officeBlindDownBtn.setIcon(icon3)
        self.officeBlindDownBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.officeBlindDownBtn)

        self.officeBlindUpBtn = QPushButton(self.frame_10)
        self.officeBlindUpBtn.setObjectName(u"officeBlindUpBtn")
        self.officeBlindUpBtn.setIcon(icon4)
        self.officeBlindUpBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.officeBlindUpBtn)


        self.verticalLayout_13.addWidget(self.frame_10)


        self.officeWidgets.addWidget(self.officeBlinds, 0, 1, 1, 1)

        self.officeAir = QWidget(self.officePage)
        self.officeAir.setObjectName(u"officeAir")
        self.verticalLayout_14 = QVBoxLayout(self.officeAir)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.officeAir)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.officeAirOptions = QFrame(self.officeAir)
        self.officeAirOptions.setObjectName(u"officeAirOptions")
        self.officeAirOptions.setFrameShape(QFrame.StyledPanel)
        self.officeAirOptions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.officeAirOptions)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.officeAirBtn = QPushButton(self.officeAirOptions)
        self.officeAirBtn.setObjectName(u"officeAirBtn")
        self.officeAirBtn.setFont(font1)
        self.officeAirBtn.setIcon(icon5)
        self.officeAirBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.officeAirBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_12 = QLabel(self.officeAirOptions)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_12, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.officeAirSpeed = QComboBox(self.officeAirOptions)
        self.officeAirSpeed.addItem("")
        self.officeAirSpeed.addItem("")
        self.officeAirSpeed.addItem("")
        self.officeAirSpeed.setObjectName(u"officeAirSpeed")
        self.officeAirSpeed.setFont(font1)
        self.officeAirSpeed.setEditable(False)

        self.horizontalLayout_14.addWidget(self.officeAirSpeed, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_14.addWidget(self.officeAirOptions)


        self.officeWidgets.addWidget(self.officeAir, 2, 0, 1, 2)

        self.HumidTemp = QWidget(self.officePage)
        self.HumidTemp.setObjectName(u"HumidTemp")
        self.verticalLayout_17 = QVBoxLayout(self.HumidTemp)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.officeTemp = QFrame(self.HumidTemp)
        self.officeTemp.setObjectName(u"officeTemp")
        self.officeTemp.setFrameShape(QFrame.StyledPanel)
        self.officeTemp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.officeTemp)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.officeTemp)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.officeTemperatureLbl = QLabel(self.officeTemp)
        self.officeTemperatureLbl.setObjectName(u"officeTemperatureLbl")
        self.officeTemperatureLbl.setFont(font1)

        self.horizontalLayout_13.addWidget(self.officeTemperatureLbl)


        self.verticalLayout_17.addWidget(self.officeTemp)

        self.officeHumid = QFrame(self.HumidTemp)
        self.officeHumid.setObjectName(u"officeHumid")
        self.officeHumid.setFrameShape(QFrame.StyledPanel)
        self.officeHumid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.officeHumid)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.officeHumid)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.officeHumidityLbl = QLabel(self.officeHumid)
        self.officeHumidityLbl.setObjectName(u"officeHumidityLbl")
        self.officeHumidityLbl.setFont(font1)

        self.horizontalLayout_12.addWidget(self.officeHumidityLbl)


        self.verticalLayout_17.addWidget(self.officeHumid)


        self.officeWidgets.addWidget(self.HumidTemp, 1, 0, 1, 2)


        self.verticalLayout_10.addLayout(self.officeWidgets)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.mainPages.addWidget(self.officePage)
        self.bedroomPage = QWidget()
        self.bedroomPage.setObjectName(u"bedroomPage")
        self.verticalLayout_7 = QVBoxLayout(self.bedroomPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.bedroomPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.mainPages.addWidget(self.bedroomPage)
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
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.serial_ports_list = QComboBox(self.ports)
        self.serial_ports_list.setObjectName(u"serial_ports_list")
        sizePolicy1.setHeightForWidth(self.serial_ports_list.sizePolicy().hasHeightForWidth())
        self.serial_ports_list.setSizePolicy(sizePolicy1)
        self.serial_ports_list.setFont(font1)

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

        self.horizontalLayout_5.addWidget(self.baudrates_list, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.budrates, 0, Qt.AlignVCenter)

        self.control_buttons = QFrame(self.settingsPage)
        self.control_buttons.setObjectName(u"control_buttons")
        self.control_buttons.setFrameShape(QFrame.StyledPanel)
        self.control_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.control_buttons)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.updateBtn = QPushButton(self.control_buttons)
        self.updateBtn.setObjectName(u"updateBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.updateBtn.sizePolicy().hasHeightForWidth())
        self.updateBtn.setSizePolicy(sizePolicy4)
        self.updateBtn.setFont(font)

        self.verticalLayout_9.addWidget(self.updateBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.connectBtn = QPushButton(self.control_buttons)
        self.connectBtn.setObjectName(u"connectBtn")
        sizePolicy4.setHeightForWidth(self.connectBtn.sizePolicy().hasHeightForWidth())
        self.connectBtn.setSizePolicy(sizePolicy4)
        self.connectBtn.setFont(font)

        self.verticalLayout_9.addWidget(self.connectBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.disconnectBtn = QPushButton(self.control_buttons)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        sizePolicy4.setHeightForWidth(self.disconnectBtn.sizePolicy().hasHeightForWidth())
        self.disconnectBtn.setSizePolicy(sizePolicy4)
        self.disconnectBtn.setFont(font)

        self.verticalLayout_9.addWidget(self.disconnectBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.control_buttons)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.mainPages.addWidget(self.settingsPage)

        self.verticalLayout_4.addWidget(self.mainPages)

        self.widget = QWidget(self.mainBodyContainer)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 38))
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, 0)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.size_grip = QFrame(self.widget)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(25, 25))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.size_grip, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.widget)


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
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon6)
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
        self.livingroomBtn.setStyleSheet(u"background-color: #52a5e0;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/tv.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.livingroomBtn.setIcon(icon7)
        self.livingroomBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.livingroomBtn)

        self.officeBtn = QPushButton(self.frame_2)
        self.officeBtn.setObjectName(u"officeBtn")
        self.officeBtn.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.officeBtn.setIcon(icon8)
        self.officeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.officeBtn)

        self.bedroomBtn = QPushButton(self.frame_2)
        self.bedroomBtn.setObjectName(u"bedroomBtn")
        self.bedroomBtn.setFont(font2)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/bed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bedroomBtn.setIcon(icon9)
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
        self.settingsBtn.setFont(font2)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon10)
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
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Persianas", None))
        self.livingBlindDownBtn.setText("")
        self.livingBlindUpBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Luces", None))
        self.livingLightsBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Aire Acondicionado", None))
        self.livingAirBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u" Velocidad", None))
        self.livingAirSpeed.setItemText(0, QCoreApplication.translate("MainWindow", u"Baja", None))
        self.livingAirSpeed.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))
        self.livingAirSpeed.setItemText(2, QCoreApplication.translate("MainWindow", u"Alta", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.livingTemperatureLbl.setText(QCoreApplication.translate("MainWindow", u"30\u00baC", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Humedad", None))
        self.livingHumidityLbl.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Luces", None))
        self.officeLightsBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Persianas", None))
        self.officeBlindDownBtn.setText("")
        self.officeBlindUpBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Aire Acondicionado", None))
        self.officeAirBtn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" Velocidad", None))
        self.officeAirSpeed.setItemText(0, QCoreApplication.translate("MainWindow", u"Baja", None))
        self.officeAirSpeed.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))
        self.officeAirSpeed.setItemText(2, QCoreApplication.translate("MainWindow", u"Alta", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.officeTemperatureLbl.setText(QCoreApplication.translate("MainWindow", u"30\u00baC", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Humedad", None))
        self.officeHumidityLbl.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dormitorio", None))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
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
    # retranslateUi

