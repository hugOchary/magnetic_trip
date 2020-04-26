class Field:

    CENTRAL = "central"

    def __init__(self, intensity, origin, distFunction=lambda x :  x, attractive=True):
        self.intensity = intensity
        self.distFunction = distFunction
        self.origin = origin
        self.attractive = attractive*(2)-1

    def getIntensity(self):
        return self.intensity
    
    def getOrigin(self):
        return self.origin
    
    def computeForce(self, distance, masse):
        return self.attractive*self.intensity*masse/self.distFunction(distance)