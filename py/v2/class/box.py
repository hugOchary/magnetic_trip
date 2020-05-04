from particle import Particle

class Box(Particle):

    def __init__(self, halfWidth, halfHeight, posX, posY, charge, mass, speedX = 0, speedY = 0):
        super().__init__(posX, posY, charge, mass, speedX, speedY)
        self.halfWidth = halfWidth
        self.halfHeight = halfHeight
    
    def getTop(self):
        return self.posY + self.halfHeight
    
    def getBot(self):
        return self.posY - self.halfHeight
    
    def getLeft(self):
        return self.posX - self.halfWidth
    
    def getRight(self):
        return self.posX + self.halfWidth
    
    def getHalfWidth(self):
        return self.halfWidth
    
    def getHalfHeight(self):
        return self.halfHeight