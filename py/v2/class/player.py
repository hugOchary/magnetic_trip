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
        self.direction = 0
        self.jumpSpeed = jumpSpeed
        self.moveSpeed = moveSpeed

    def goDirection(self, direction):
        self.direction = direction
    
    def stopDirection(self, direction):
        if self.direction == direction:
            self.direction = 0
    
    def jump(self):
        self.speedY += self.jumpSpeed
    
    def moveInDirection(self, timeDelta):
        self.posX += self.direction*self.moveSpeed*timeDelta
