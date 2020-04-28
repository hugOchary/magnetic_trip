class particle:

    def __init__(self, , posX, posY, charge, mass, speedX = 0, speedY = 0):
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
    
    def getSpeedX():
        return self.speedX

    def getSpeedY():
        return self.speedY