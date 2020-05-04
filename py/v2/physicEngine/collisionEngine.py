from importer import *
import numpy as np

def collisionSolver(box1, box2):
    '''
    Returns the new positionafter collision resolution
    '''

    posX = box1.getX()
    posY = box1.getY()

    reverseSpeedVect = (-box1.getSpeedX(), -box1.getSpeedY())

    signX = np.sign(reverseSpeedVect[0])
    signY = np.sign(reverseSpeedVect[1])

    absMinDistance = box1.getHalfWidth() + box2.getHalfWidth()
    ordMinDistance = box1.getHalfHeight() + box2.getHalfHeight()

    absDist = box2.getX() - posX
    ordDist = box2.getY() - posY


    absDisplace = absDist + signX*absMinDistance
    ordDisplace = ordDist + signY*ordMinDistance

    
    newPosX = posX + absDisplace
    newPosY = posY + ordDisplace

    if signX == 0:
        return (0, ordDisplace)
    elif signY == 0:
        return (absDisplace, 0)
    else :
        (affA, affB) = toAffineFunction(
            reverseSpeedVect[0],
            reverseSpeedVect[1],
            posX,
            posY)
        testPosY = affA*newPosX + affB
        testPosX = (newPosY - affB)/affA

        dist1 = distanceSquare(posX, posY, newPosX, testPosY)
        dist2 = distanceSquare(posX, posY, testPosX, newPosY)

        if dist1 <= dist2:
            return (newPosX-posX, testPosY-posY)
        else :
            return (testPosX-posX, newPosY-posY)

    

def boxCollisionDetector(box1, box2):
    '''
    Return true if box1 and box2 overlap
    '''
    if box1 is box2:
        return false
    absDist = abs(box1.getX() - box2.getX())
    ordDist = abs(box1.getY() - box2.getY())
    return (
        (box1.getHalfWidth() + box2.getHalfWidth()) > absDist
        and (box1.getHalfHeight() + box2.getHalfHeight()) > ordDist
    )


def sortAndSweepCollisionSolver(box, sortedBoxList):
    '''
    Return the displacement required to avoid collision
    '''
    #We build the dictionary of all "active" box that could Collide with our box
    left = box.getLeft()
    right = box.getRight()
    index = 0
    activeDict = {}
    n = len(sortedBoxList)
    resX = 0
    resY = 0

    while index < n and sortedBoxList[index][0] < left:
        if (sortedBoxList[1] == 'r'):
            activeDict.pop(sortedBoxList[index][2])
        else:
            activeDict[sortedBoxList[index][2]] = 'active'
        index+=1

    #We check if all active box collide with our box
    for activeBox in activeDict.keys():
        #Detection : Using left right top bot overlapping
        if boxCollisionDetector(box, activeBox):

            #Resolution : 
            (dX, dY) = collisionSolver(box, activeBox)
            resX = selectExtreme(dX, resX)
            resY = selectExtreme(dY, resY)

    while index < n and sortedBoxList[index][0] <= right:
        #Detection : Using left right top bot overlapping
        if boxCollisionDetector(box, sortedBoxList[index][2]):

            #Resolution : 
            (dX, dY) = collisionSolver(box, sortedBoxList[index][2])
            resX = selectExtreme(dX, resX)
            resY = selectExtreme(dY, resY)

        index+=1
    return (resX, resY)

def indexInsertSorted(element, elementList):
    
    index = 0

    if elementList == []:
        return index 
    
    while index < len(elementList) and elementList[index][0] < element:
        index+=1
    
    return index

def selectExtreme(value1, value2):
    if (value1 < 0 and value1 < value2) or (value1 > 0 and value1 > value2):
        return value1
    else:
        return value2

def closestToZero(value1, value2):
    if abs(value1) <= abs(value2):
        return value1
    return value2

def furthestToZero(value1, value2):
    if abs(value1) <= abs(value2):
        return value2
    return value1

def toAffineFunction(vectX, vectY, posX, posY):
    '''
    return the affine function Y = aX + b 
    directed by (vectX, vectY) going through (posX, poY)
    '''
    if vectX == 0:
        return (0,0)
    elif vectY == 0:
        return (0, posY)
    else:
        resA = vectY/vectX
        resB = posY - posX*resA
        return (resA, resB)

def distanceSquare(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2