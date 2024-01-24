# DomoticHouse
piuic describir comando y pyrcc__


Generate exe: 
pyinstaller --onefile --noconsole 
--add-data="icons\*;." 
--add-data="ui_DomoticApp.py;." 
--add-data="resources_rc.py;." 
--add-data="Wifi.py;."
--add-data="SerialConnection.py;."
--add-data="CommunicationController.py;."
--add-data="Room.py;."
--add-data="RoomUi.py;."
--add-data="RoomController.py;."
--hiddenimport=PySide2.QtPrintSupport --icon=icons\window-icon.ico --name DomoticApp 
mainApp.py

