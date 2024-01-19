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
        print(line)
        if not (line.startswith('{') and line.endswith('}')): return None
        try: return json.loads(line)
        except: return None
    
    def read(self):
        if not self.serial.waitForReadyRead(500): return None
        line = self.serial.readLine().data().decode()
        if "\n" in line: print("Hay un salto de linea")
        return line
    
    def clear(self):
        self.serial.clear(QSerialPort.AllDirections)