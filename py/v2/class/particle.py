class Particle:

    def __init__(self, posX, posY, charge, mass, speedX = 0, speedY = 0):
        self.posX = posX
        self.posY = posY
        self.charge = charge
        self.mass = mass
        self.speedX = speedX
        self.speedY = speedY

    def getX(self):
        return self.posX
    
    def getY(self):
        return self.posY
    
    def getCharge(self):
        return self.charge
    
    def getMass(self):
        return self.mass
    
    def getSpeedX(self):
        return self.speedX

    def getSpeedY(self):
        return self.speedY
    
    def updateSpeed(self, speedTuple):
        self.speedX = speedTuple[0]
        self.speedY = speedTuple[1]
    
    def updatePos(self, posTuple):
        self.posX = posTuple[0]
        self.posY = posTuple[1]
    
    def forceDisplace(self, vect):
        self.posX+=vect[0]
        self.posY+=vect[1]
        self.speedX = 0
        self.speedY = 0
    
    def increaseMass(self, increaseValue):
        self.mass += increaseValue

    def display(self):
        print("object is at x : {0} y : {1} going at x : {2} and y : {3}".format(
            self.posX, self.posY, self.speedX, self.speedY))