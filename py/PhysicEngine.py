from physicObject import PhysicObject
from field import Field
import importlib

#physicObjectModule = "physicObject"
#collisionDetectorModule = "collisionDetector"
#importlib.import_module(physicObject)
#importlib.import_module(collisionDetector)

class PhysicEngine:

    TIME_UNIT = 1

    @classmethod
    def rectangleCollisionDetector(cls, obj1, obj2):
        ## Detect the collision betwen two rectangle objects based on overlapping boundaries
        ## The use-case will be a dynamic(obj1)/static(obj2) collison
        absDist = abs(obj1.getAbs() - obj2.getOrd)
        ordDist = abs(obj1.getOrd() - obj2.getOrd())

        minAbsDist = obj1.getHalfWidth() + obj2.getHalfWidth
        minOrdDist = obj1.getHalfHeight() + obj2.getHalfHeight

        return absDist >= minAbsDist and ordDist >= minOrdDist

    @classmethod
    def collisionSolver(cls, obj1, obj2):
        ## Compute how much obj1 needs to bounce back to get out of obj2 boundaries
        ## It is a dynamic(obj1)/static(obj2) collision
        vAbs = obj1.getVAbs()
        vOrd = obj1.getVOrd()

        abs1 = obj1.getAbs()
        abs2 = obj2.getAbs()

        ord1 = obj1.getOrd()
        ord2 = obj2.getOrd()

        alpha = min(
            (abs1-abs2)/vAbs + (obj1.getHalfWidth()+obj2.getHalfWidth())/abs(vAbs),
            (ord1-ord2)/vOrd + (obj1.getHalfHeight()+obj2.getHalfHeight())/abs(vOrd),
        )

        return alpha

    def __init__(self, gravity=10):

        # L'ensemble des champs qui modifieront l'accélération 
        self.fields = []

        # L;intensité du champ de gravité global
        self.gravity = gravity
    
    def accelerationPhase(self, objects):
        ## Compute for each dynamic object its acceleration
        ## Acceleration depends only on the different fields
        ## TODO add friction on surfaces
        ## TODO add movement friction to create different environments
        for obj in objects:
            if obj.physic == PhysicObject.DYNAMIC:
                resAbs = 0
                resOrd = -10
                for field in self.fields:
                    if (field.getOrigin() == obj):
                        pass
                    distAbs = obj.getAbs() - field.getOrigin().getAbs
                    distOrd = obj.getOrd() - field.getOrigin().getOrd
                    acc = field.computeForce(abs(distAbs) + abs(distOrd))
                    resAbs += acc/distAbs
                    resOrd += acc/distOrd
                obj.setAcceleration(resAbs, resOrd)
    
    def speedPhase(self, objects):
        ## All dynamic objects update their speed based on previous speed
        ## acceleration and TIME_UNIT
        ## TODO Allow modifiction of TIME_UNIT to create timewarp effect
        for obj in objects:
            obj.computeSpeed(PhysicEngine.TIME_UNIT)
            obj.translate(PhysicEngine.TIME_UNIT)
    
    def computeCollisions(self, dynamics, statics):
        ## We detect and resolve all collisions
        ## If multiple collisions with different static objects
        ## we move the dynamic object once such that all collisions are solved
        for obj1 in dynamics:
            alpha = 0
            for obj2 in statics:
                if (PhysicEngine.rectangleCollisionDetector(obj1, obj2)):
                    alpha = max(alpha, PhysicEngine.collisionSolver(obj2, obj2))
            if alpha != 0:
                obj1.warpSpeed(-alpha)
                obj1.translate(PhysicEngine.TIME_UNIT)

    
