# DomoticHouse
piuic describir comando y pyrcc__


Generate exe: pyinstaller --onefile --noconsole --add-data="icons\*;." --add-data="ui_DomoticApp.py;." --add-data="resources_rc.py;." --hiddenimport=PySide2.QtPrintSupport --icon=icons\window-icon.ico --name DomoticApp mainApp.py