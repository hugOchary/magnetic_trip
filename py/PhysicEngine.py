import physicObject
import collisionDetector
import importlib

physicObjectModule = "physicObject"
collisionDetectorModule = "collisionDetector"
importlib.import_module(physicObject)
importlib.import_module(collisionDetector)

class PhysicEngine:

    def __init__(self):
        #Rien à mettre pour l'instant#
        self.fields = []
    
    def accelerationPhase(objects):
        for o in objects:
            if o.physic == physicObject.DYNAMIC:
                for field in fields:
                    distAbs = abs(o.getAbs() - field.getOrigin())
                    break
            break
    
