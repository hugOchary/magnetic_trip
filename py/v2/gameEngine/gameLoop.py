from importer import *

def buildSortedBoxList(staticObjectList):
    sortedBoxList = []
    for rect in staticObjectList:
        sortedBoxList.insert(
            indexInsertSorted(rect.getLeft(), sortedBoxList),
            (rect.getLeft(), 'l', rect)
        )
        sortedBoxList.insert(
            indexInsertSorted(rect.getRight(), sortedBoxList),
            (rect.getRight(), 'r', rect)
        )
    return sortedBoxList

def eventHandling(controlHandler):
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN:
            controlHandler.handlePress(event)
        elif event.type == pygame.KEYUP:
            controlHandler.handleRelease(event)
    return running

def playerMovementLoop(player, sortedBoxList, timeDelta):
    player.startMoving()
    player.moveInDirection(timeDelta)
    playerCollision(player, sortedBoxList)
    player.stopMoving()
    return player

def physicLoop(
    player, sortedBoxList, 
    objectList, fieldList, 
    globalFieldList, timeDelta, 
    envMod):
    loop(objectList, fieldList, globalFieldList, timeDelta, envMod)
    playerCollision(player, sortedBoxList)
    return player

def playerCollision(player, sortedBoxList):
    displaceVect = sortAndSweepCollisionSolver(player, sortedBoxList)
    if displaceVect != (0,0):
        player.forceDisplace(displaceVect)
    return player
