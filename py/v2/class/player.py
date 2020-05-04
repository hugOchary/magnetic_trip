from box import Box

class Player(Box):
    def __init__(
        self,
        jumpSpeed,
        moveSpeed, 
        halfWidth, 
        halfHeight, 
        posX, 
        posY, 
        charge, 
        mass, 
        speedX = 0, 
        speedY = 0):
        
        super().__init__(
            halfWidth, 
            halfHeight, 
            posX, posY, 
            charge, 
            mass, 
            speedX = 0, 
            speedY = 0)
        self.jumpSpeed = jumpSpeed
        self.moveSpeed = moveSpeed

        self.direction = 0
        self.isMoving = False
        self.speedStash = ()
        self.isStashed = False
        self.canJump = False

    def startDirection(self, direction):
        self.direction = direction
    
    def stopDirection(self, direction):
        if self.direction == direction:
            self.direction = 0
    
    def jump(self):
        if self.canJump:
            self.speedY = self.jumpSpeed
            self.canJump = False
    
    def moveInDirection(self, timeDelta):
        self.posX += self.direction*self.moveSpeed*timeDelta
    
    def forceDisplace(self, vect):
        self.posX+=vect[0]
        self.posY+=vect[1]
        self.speedX = 0
        self.speedY = 0
        if not self.isStashed:
            self.canJump = True

    
    def startMoving(self):
        self.storeInSpeedStash()
        self.speedX = self.direction*self.moveSpeed
        self.speedY = 0
    
    def stopMoving(self):
        self.retrieveFromSpeedStash()
    
    def storeInSpeedStash(self):
        self.speedStash = (self.speedX, self.speedY)
        self.isStashed = True
    
    def retrieveFromSpeedStash(self):
        self.speedX = self.speedStash[0]
        self.speedY = self.speedStash[1]
        self.speedStash = ()
        self.isStashed = False

    
