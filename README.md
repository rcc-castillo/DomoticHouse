# DomoticHouse
Para el correcto funcionamiento del servidor se debe incluir un archivo llamado `WifiCredentials.h` en la carpeta `ESP8266Code` con el siguiente contenido:
```cpp
#ifndef Credentials_h
#define Credentials_h

const char *ssid = ""; // Nombre de la red wifi
const char *password = ""; // Contraseña de la red wifi

#endif
```

Para desplegar la aplicación se debe emplear el comando:
```bash
pyinstaller --onefile --noconsole --add-data="icons\*;." --add-data="ui_DomoticApp.py;." --add-data="resources_rc.py;." --add-data="Wifi.py;." --add-data="SerialConnection.py;." --add-data="CommunicationController.py;." --add-data="Room.py;." --add-data="RoomUiController.py;." --add-data="RoomController.py;." --hiddenimport=PySide2.QtPrintSupport --icon=icons\window-icon.ico --name DomoticApp mainApp.py
```
