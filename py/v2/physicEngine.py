import importer
import math

def computeDistance(xObj, yObj, xField, yField):
    '''
    Return the distance between obj and field
    '''
    return math.sqrt(((xObj-xField)**2)+((yObj-yField)**2))

def toVect(xObj, yObj, xField, yField, distance):
    '''
    Return a unitary vector going from obj to field
    '''
    return (
        (xObj-xField)/distance, 
        (yObj-yField)/distance
        )

def computeAxisDeltaSpeed(massObj, force, timeDelta):
    '''
    Compute the speed modification caused by force 
    Only on one axis
    '''
    return (force/massObj)*timeDelta

def computeAxisNewSpeed(speed, massObj, force, timeDelta):
    return speed + computeAxisDeltaSpeed(massObj, force, timeDelta)

def computeAxisNewPosition(position, speed, timeDelta):
    return position + speed*timeDelta

def computeFieldInfluence(distSquare, massObj, massField, envMod):
    return -1*massObj*massField*envMod/distSquare

def computeVectField(vectObjField, fieldInfluence):
    return (
        vectObjField[0]*fieldInfluence,
        vectObjField[1]*fieldInfluence
        )

def computeForceAllField(obj, fieldList, envMod):
    forceX = 0
    forceY = 0
    xObj = obj.getX()
    yObj = obj.getY()
    massObj = obj.getMass()
    for field in fieldList:
        #Field parameters
        xField = field.getX()
        yField = field.getY()
        massField = field.getMass()
        #Field computation
        distance = computeDistance(xObj, yObj, xField, yField)
        vectObjField = toVect(xObj, yObj, xField, yField, distance)
        fieldInfluence = computeFieldInfluence(
            distance*distance, massObj, massField, envMod)
        fieldInfluenceVect = computeVectField(vectObjField, fieldInfluence)
        forceX = forceX + fieldInfluenceVect[0]
        forceY = forceY + fieldInfluenceVect[1]
    return (forceX, forceY)

def computeNewObjSpeed(obj, fieldList, timeDelta, envMod):
    speedX = obj.getSpeedX()
    speedY = obj.getSpeedY()
    massObj = obj.getMass()
    (forceX, forceY) = computeForceAllField(obj, fieldList, envMod)
    speedX += computeAxisDeltaSpeed(massObj, forceX, timeDelta)
    speedY += computeAxisDeltaSpeed(massObj, forceY, timeDelta)
    return (speedX, speedY)

def computeNewObjPos(obj,timeDelta):
    xObj = computeAxisNewPosition(obj.getX(), obj.getSpeedX(), timeDelta)
    yObj = computeAxisNewPosition(obj.getY(), obj.getSpeedY(), timeDelta)
    return (xObj, yObj)

