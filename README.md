# DomoticHouse
El presente proyecto se basa en el diseño y desarrollo de un sistema domótico de bajo costo orientado a viviendas particulares, así como, una aplicación para ordenador capaz de comunicarse con el sistema para controlarlo.
Se pretende que este sistema sea capaz de comunicarse con la aplicación por medio de dos métodos diferente, el primero de ellos mediante el envío y recepción de datos en una conexión serial que en este caso será USB, el segundo método consta de una conexión inalámbrica por medio de tecnología wifi, en este método el cliente realizará peticiones al servidor que aloja el sistema para realizar ciertas acciones de control sobre los dispositivos de la habitación.
Con esto se pretende realizar un sistema asequible en precio, y simple para comprender las bases de los sistemas domóticos y la comprensión de las comunicaciones wifi y serial, también se pretende aprender a desarrollar una aplicación completa y a desplegarla en distintos los distintos formatos de cada sistema operativo.

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
