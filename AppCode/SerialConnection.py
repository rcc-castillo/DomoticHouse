from PySide2.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide2 import QtCore
import json

class SerialConnection():
    def __init__(self):
        self.serial = QSerialPort()
        self.connected = False
    
    def open(self, portName, baudRate):
        self.serial.setPortName(portName)
        self.serial.setBaudRate(baudRate)
        self.serial.open(QtCore.QIODevice.ReadWrite)
        self.connected = self.serial.isOpen()
    
    def close(self):
        self.serial.close()
        self.connected = self.serial.isOpen()
    
    def getPorts(self):
        ports = []
        for port in QSerialPortInfo.availablePorts():
            ports.append(port.portName())
        return ports
    
    def get(self, endpoint):
        self.serial.write(f"{endpoint}\n".encode())
        if not self.serial.waitForBytesWritten(500): return None
        line = self.read()
        print("Recibido: ", line)
        if line is None: return None
        if not (line.startswith('{') and line.endswith('}')): return None
        try: return json.loads(line)
        except: return None
    
    def read(self):
        self.serial.waitForReadyRead(200)
        try: line = self.serial.readLine().data().decode().strip()
        except: return None
        return line
    
    def write(self, data):
        self.serial.write(f"{data}\n".encode())
        if not self.serial.waitForBytesWritten(1000): return None
    
    def clear(self):
        self.serial.clear(QSerialPort.AllDirections)
        error = self.serial.error()
        if error != QSerialPort.NoError:
            print("Error clearing serial port:", error)

    def isConnected(self):
        return self.connected