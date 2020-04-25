class field:

    CENTRAL = "central"

    def __init__(self, intensity, distFunction, origin):
        self.intensity = intensity
        self.distFunction = distFunction
        self.origin = origin

    def getIntensity(self):
        return self.intensity
    
    def getOrigin(self):
        return self.origin
    
    def computeForce(self, distance, masse):
        return self.intensity*masse/self.distFunction(distance)