

class PhysicObject:

    DYNAMIC = "dynamic"
    STATIC = "static"

    def __init__(self, height, width, mass, physic=PhysicObject.STATIC):
        self.height = height
        self.width = width
        self.mass = mass
        self.physic = physic

        self.absc = 0
        self.ordo = 0

        self.vAbs = 0
        self.vOrd = 0

        self.aAbs = 0
        self.aOrd = 0

    def getAbs(self):
        return self.absc
    
    def getOrd(self):
        return self.ordo

    def getHalfHeight(self):
        return self.height/2
    
    def getHalfWidth(self):
        return self.width/2
    
    def getVAbs(self):
        return self.vAbs
    
    def getVOrd(self):
        return self.vOrd

    def setAbsc(self, absc):
        self.absc = absc
    
    def setordo(self, ordo):
        self.ordo = ordo

    def setSpeed(self, vAbs, vOrd):
        self.vAbs = vAbs
        self.vOrd = vOrd
    
    def setAcceleration(self, aAbs, aOrd):
        self.aAbs = aAbs
        self.aOrd = aOrd
    
    def computeSpeed(self, timeUnit):
        self.vAbs = self.vAbs + self.aAbs*timeUnit
        self.vOrd = self.vOrd + self.aOrd*timeUnit
    
    def warpSpeed(self, alpha):
        self.vAbs *= alpha
        self.vOrd *= alpha

    def translate(self, timeUnit):
        self.absc = self.absc + self.vAbs*timeUnit
        self.ordo = self.ordo + self.vOrd*timeUnit

    