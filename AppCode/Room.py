class Room():
    def __init__(self, name, window, lights=None, blinds=None, air=None, humidTemp=None,irrigation=None):
        self.name = name
        self.lights = lights
        self.blinds = blinds
        self.air = air
        self.irrigation = irrigation
        self.humidTemp = humidTemp
        self.window = window

    def handleLights(self, state):
        self.lights["state"] = state
    
    def handleBlinds(self, direction):
        if self.blinds == direction: return
        self.blinds["state"] = direction
    
    def handleAir(self, state):
        self.air["state"] = state

    def handleAirSpeed(self, speed):
        self.air["speed"] = speed
    
    def handleIrrigation(self, state):
        self.irrigation["state"] = state

    def handleIrrigationStartTime(self, time):
        self.irrigation["startTime"] = time
    
    def handleIrrigationEndTime(self, time):
        self.irrigation["endTime"] = time

    def handleHumidTemp(self, temperature, humidity):
        self.humidTemp["temperature"] = temperature
        self.humidTemp["humidity"] = humidity

    def getElement(self, element):
        return getattr(self, element, None)
