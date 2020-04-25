

class PhysicObject:

    DYNAMIC = "dynamic"
    STATIC = "static"

    def __init__(self, height, width, mass, physic=PhysicObject.STATIC) {
        self.height = height
        self.width = width
        self.mass = mass
        self.physic = physic

        self.abs = 0
        self.ord = 0

        self.vAbs = 0
        self.vOrd = 0

        self.aAbs = 0
        self.aOrd = 0
    }

    def getAbs(self):
        return self.abs
    
    def getOrd(self):
        return self.ord

    def getHalfHeight(self):
        return self.height/2
    
    def getHalfWidth(self):
        return self.width/2

    def setSpeed(vAbs, vOrd):
        self.vAbs = vAbs
        self.vOrd = vOrd
    

    