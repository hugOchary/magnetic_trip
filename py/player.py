
from physicObject import PhysicObject

class Player(PhysicObject):
    
    LEFT = 0
    RIGHT = 1

    MOVE_SPEED = 20

    def __init__(self, height, width, ordo, absc, mass=1, physic=PhysicObject.STATIC):
        super().__init__(height, width, ordo, absc, mass, physic)

        self.isMoving = True
        self.direction = None
        self.hasLanded = False

    def goLeft(self):
        self.addVAbs(-50*(1+self.isMoving*(self.direction == self.RIGHT)))
        self.isMoving = True
        self.direction = self.LEFT
    
    def goRight(self):
        self.addVAbs(50*(1+self.isMoving*(self.direction == self.LEFT)))
        self.isMoving = True
        self.direction = self.RIGHT

    def stop(self, direction):
        if self.isMoving and direction == self.direction:
            self.addVAbs(50*(self.direction == self.LEFT) - 50*(self.direction == self.RIGHT))
            self.isMoving = False
    
    def speedReset(self):
        self.setSpeed(0,0)
        if self.isMoving:
            self.addVAbs(-50*(self.direction == self.LEFT) + 50*(self.direction == self.RIGHT))
    
    def jump(self):
        if self.hasLanded:
            self.addVOrd(-50)
            self.hasLanded = False
    
    def bounce(self, delta):
        self.hasLanded = delta[0] != 0
        self.absc = self.absc + delta[0]
        self.ordo = self.ordo + delta[1]

