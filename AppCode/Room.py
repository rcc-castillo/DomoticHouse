class Room():
    def __init__(self, name, lights=None, blinds=None, air=None, humidtemp=None,irrigation=None):
        self.name = name
        self.lights = lights
        self.blinds = blinds
        self.air = air
        self.irrigation = irrigation
        self.humidtemp = humidtemp

    def handleLightsState(self, state):
        self.lights["state"] = state
    
    def handleBlindsState(self, direction):
        if self.blinds == direction: return
        self.blinds["state"] = direction
    
    def handleAirState(self, state):
        self.air["state"] = state

    def handleAirSpeed(self, speed):
        self.air["speed"] = speed
    
    def handleIrrigationState(self, state):
        self.irrigation["state"] = state

    def handleIrrigationStartTime(self, time):
        self.irrigation["startTime"] = time
    
    def handleIrrigationEndTime(self, time):
        self.irrigation["endTime"] = time

    def handleHumidTemp(self, data):
        self.humidtemp = data

    def getDevice(self, deviceName):
        return getattr(self, deviceName.lower(), None)
    
    def getHandler(self, deviceName, deviceElement):
        return getattr(self, f"handle{deviceName}{deviceElement}", None)
