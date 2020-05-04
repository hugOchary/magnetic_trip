from importer import *

WIDTH = 1080
HEIGHT = 720

if __name__ == "__main__":
    '''
    Simple script to test movement and collision
    '''

    player = Player(
        jumpSpeed = 50,
        moveSpeed = 40,
        halfWidth=25,
        halfHeight=25,
        posX=200,
        posY=200,
        charge=0,
        mass=1,
        speedX=40,
        speedY=40
    )

    ground = Box(
        halfWidth=WIDTH/2,
        halfHeight=20,
        posX=0,
        posY=-HEIGHT/2,
        charge=0,
        mass=1,
        speedX=0,
        speedY=0
    )

    lWall = Box(
        halfWidth=20,
        halfHeight=HEIGHT//2,
        posX=-WIDTH//2,
        posY=0,
        charge=0,
        mass=1,
        speedX=0,
        speedY=0
    )

    rWall = Box(
        halfWidth=20,
        halfHeight=HEIGHT//2,
        posX=WIDTH//2,
        posY=0,
        charge=0,
        mass=1,
        speedX=0,
        speedY=0
    )

    blackHole = Particle(
        posX=0, 
        posY=0, 
        charge=0, 
        mass=300000)

    globalField = (0,-10)

    renderer = Renderer(WIDTH, HEIGHT, 'jump')
    controlHandler = ControlHandler(player)

    clock = pygame.time.Clock()
    running = True

    rectList = [ground, lWall, rWall, player]
    globalFieldList = [globalField]
    objectList = [player]
    staticObjectList = [ground, lWall, rWall]
    fieldList = [blackHole]
    timeDelta = 0.1
    envMod = 1

    sortedBoxList = []

    

    while running:

        #we build the sorted list of all absciss
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

        #We resolve user inputs and game mecanic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                controlHandler.handlePress(event)
            elif event.type == pygame.KEYUP:
                controlHandler.handleRelease(event)
        player.moveInDirection(timeDelta)

        #We execute the physic simulation
        loop(objectList, fieldList, globalFieldList, timeDelta, envMod)
        displaceVect = sortAndSweepCollisionSolver(player, sortedBoxList)
        if displaceVect != (0,0):
            player.forceDisplace(displaceVect)

        #We draw the result on the screen
        renderer.reset()
        renderer.drawCircle(blackHole.getX(), blackHole.getY(), 30)
        for rect in rectList:
            renderer.drawRect(
                rect.getX(), 
                rect.getY(), 
                rect.getHalfWidth(), 
                rect.getHalfHeight()
            )
        renderer.update()

        player.display()
        clock.tick(120)