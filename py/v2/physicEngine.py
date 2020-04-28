import importer

def computeDistance(xObj, yObj, xField, yField):
    return (xObj-xField)**2+(yObj-yField)**2

def computeAxisDeltaSpeed(massObj, force, timeDelta):
    '''
    Compute the speed modification caused by force 
    Only on one axis
    '''
    return (force/massObj)*timeDelta

def computeAxisNewSpeed(speed, massObj, force, timeDelta):
    return speed + computeAxisDeltaSpeed(massObj, force, timeDelta)

def computeAxisNewPosition(position, speed, timedelta):
    return position + speed*timeDelta

def computeFieldInfluence(distSquare, chargeObj, chargeField, envMod):
    return chargeObj*chargeField*envMod/distSquares

def computeAxisField(posObj, posField, distSquare, fieldInfluence):
    return fieldInfluence*(posObj-posField)**2/distSquare

def computeForceAllField(obj, fieldList, envMod):
    forceX = 0
    forceY = 0
    xObj = obj.getX()
    yObj = obj.getY()
    chargeObj = obj.getCharge()
    for field in fieldList:
        xfield = field.getX()
        yField = field.getY()
        chargeField = field.getCharge()
        distSquare = computeDistance(xObj, yObj, xField, yField)
        fieldInfluence = computeFieldInfluence(distSquare, chargeObj, chargeField, envMod)
        forceX = forceX + computeAxisField(xObj, xField, distSquare, fieldInfluence)
        forceY = forceY + computeAxisField(yObj, yField, distSquare, fieldInfluence)
    return (forceX, forceY)

def computeNewObjSpeed(obj, fieldList, timeDelta, envMod):
    speedX = obj.getSpeedX()
    speedY = obj.getSpeedY()
    massObj = obj.getMasse()
    (forceX, forceY) = computeForceAllField(obj, fieldList, envMod)
    speedX += computeAxisDeltaSpeed(massObj, forceX, timeDelta)
    speedY += computeAxisDeltaSpeed(massObj, forceY, timeDelta)
    return (speedX, speedY)

def computeNewObjPos(obj, speedX, speedY, timeDelta):
    xObj = computeAxisNewPosition(obj.getX(), speed, timedelta)
    yObj = computeAxisNewPosition(obj.getY(), speed, timeDelta)
    return (xObj, yObj)

