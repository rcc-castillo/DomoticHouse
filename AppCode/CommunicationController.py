import json
from Wifi import Wifi
from SerialConnection import SerialConnection

SERVER_URL = 'http://192.168.195.249/'

class CommunicationController:
    def __init__(self):
        self.wifi = Wifi(SERVER_URL)
        self.serial = SerialConnection()

        self.ENDPOINTS = {
            "getData": "getData",
            "getRooms": "getRooms",
            "Lights": "sendLights",
            "Blinds": "sendBlinds",
            "Air": "sendAir",
            "Irrigation": "sendIrrigation"
        }

    def sendData(self, roomName, deviceName, deviceElement, data):
        print(f"Sending {deviceName} {deviceElement} {data} to {roomName}")
        json_data = json.dumps({roomName: {deviceName: data.lower()}})
        if self.wifi.isConnected():
            endpoint = self.ENDPOINTS[deviceName]
            arguments = f"?roomName={roomName}&deviceName={deviceName}&deviceElement={deviceElement}"
            self.wifi.post(f"{endpoint}{arguments}", json_data)
        elif self.serial.isConnected():
            self.serial.write(f"{roomName},{deviceName},{deviceElement},{json_data}")
            print(self.serial.read())
        else:print("No hay conexión")

    def getData(self):
        if self.wifi.connected:
            data = self.wifi.get(self.ENDPOINTS["getData"])
        elif self.serial.connected:
            data = self.serial.get("getData")
        else: return
        
        if data is None: return print("No se pudo obtener la data")
        return data

    def getRooms(self):
        if self.wifi.connected:
            data = self.wifi.get(self.ENDPOINTS["getRooms"])
        elif self.serial.connected:
            data = self.serial.get("getRooms")
        else: return
        
        if data is None: return
        return data

    def getSerialPorts(self):
        return self.serial.getPorts()
    
    def serialConnect(self, port, baudrate):
        return self.serial.open(port, baudrate)
    
    def serialDisconnect(self):
        if not self.serialIsConnected:
            self.serialClear()
        return self.serial.close()
    
    def serialClear(self):
        return self.serial.clear()
    
    def serialIsConnected(self):
        return self.serial.isConnected()
    
    def wifiConnect(self):
        return self.wifi.connect()
    
    def wifiDisconnect(self):
        return self.wifi.disconnect()
    
    def wifiIsConnected(self):
        return self.wifi.isConnected()
    
    def toggleConnectionMethod(self):        
        if self.wifiIsConnected():
            self.wifiDisconnect()
        else:
            self.serialDisconnect()
            self.wifiConnect()
        