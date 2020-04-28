class PhysicObject:

    DYNAMIC = "dynamic"
    STATIC = "static"

    def __init__(self, height, width, ordo, absc, mass=1, physic=STATIC):
        self.height = height
        self.width = width
        self.mass = mass
        self.physic = physic

        self.absc = absc
        self.ordo = ordo

        self.vAbs = 0
        self.vOrd = 0

        self.aAbs = 0
        self.aOrd = 0
    
    ## GETTERS

    def getMass(self):
        return self.mass

    def getAbs(self):
        return self.absc
    
    def getOrd(self):
        return self.ordo
    
    def getCoord(self):
        return (self.absc, self.ordo)

    def getHalfHeight(self):
        return self.height/2
    
    def getHalfWidth(self):
        return self.width/2
    
    def getVAbs(self):
        return self.vAbs
    
    def getVOrd(self):
        return self.vOrd
    
    def getSpeed(self):
        return (self.vAbs, self.vOrd)

    def getAcc(self):
        return (self.aAbs, self.aOrd)

    ## SETTERS

    def setAbs(self, absc):
        self.absc = absc
    
    def setOrd(self, ordo):
        self.ordo = ordo

    def setVAbs(self, vAbs):
        self.vAbs = vAbs
    
    def setVOrd(self, vOrd):
        self.vOrd = vOrd
    
    def addVAbs(self, vAbs):
        self.vAbs += vAbs
    
    def addVOrd(self, vOrd):
        self.vOrd += vOrd

    def setSpeed(self, vAbs, vOrd):
        self.vAbs = vAbs
        self.vOrd = vOrd
    
    def speedReset(self):
        self.setSpeed(0,0)
    
    def setAcceleration(self, aAbs, aOrd):
        self.aAbs = aAbs
        self.aOrd = aOrd

    ## COMPUTATIONS
    
    def computeSpeed(self, timeUnit):
        self.vAbs = self.vAbs + self.aAbs*timeUnit
        self.vOrd = self.vOrd + self.aOrd*timeUnit
    
    def warpSpeed(self, alpha):
        self.vAbs *= alpha
        self.vOrd *= alpha

    def translate(self, timeUnit):
        self.absc = self.absc + self.vAbs*timeUnit
        self.ordo = self.ordo + self.vOrd*timeUnit
    
    def bounce(self, delta):
        self.absc = self.absc + delta[0]
        self.ordo = self.ordo + delta[1]

    def isMoving(self):
        return self.vAbs != 0 or self.vOrd != 0
    