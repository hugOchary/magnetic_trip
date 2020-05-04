from importer import *
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
    if distance == 0:
        return (0,0)
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
    if distSquare == 0:
        return 0
    return -1*massObj*massField*envMod/distSquare

def computeVectField(vectObjField, fieldInfluence):
    return (
        vectObjField[0]*fieldInfluence,
        vectObjField[1]*fieldInfluence
        )

def computeForceAllField(obj, fieldList, globalFieldList, envMod):
    forceX = 0
    forceY = 0
    xObj = obj.getX()
    yObj = obj.getY()
    massObj = obj.getMass()
    for globalField in globalFieldList:
        forceX += massObj*globalField[0]
        forceY += massObj*globalField[1]
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
    #print(forceX, forceY)
    return (forceX, forceY)

def computeNewObjSpeed(obj, fieldList, globalFieldList, timeDelta, envMod):
    speedX = obj.getSpeedX()
    speedY = obj.getSpeedY()
    massObj = obj.getMass()
    (forceX, forceY) = computeForceAllField(obj, fieldList, globalFieldList, envMod)
    speedX += computeAxisDeltaSpeed(massObj, forceX, timeDelta)
    speedY += computeAxisDeltaSpeed(massObj, forceY, timeDelta)
    #print(max(min(speedX, 100), -100), max(min(speedY,1000), -100))
    return (speedX, speedY)

def computeNewObjPos(obj,timeDelta):
    xObj = computeAxisNewPosition(obj.getX(), obj.getSpeedX(), timeDelta)
    yObj = computeAxisNewPosition(obj.getY(), obj.getSpeedY(), timeDelta)
    #print(xObj, yObj)
    return (xObj, yObj)

#not functional
def loop(objetList, fieldList, globalFieldList, timeDelta, envMod):
    for obj in objetList:
        obj.updateSpeed(
            computeNewObjSpeed(obj, fieldList, globalFieldList, timeDelta, envMod)
        )
        obj.updatePos(
            computeNewObjPos(obj, timeDelta)
        )

