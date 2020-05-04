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
        posX=0,
        posY=-325,
        charge=0,
        mass=1
    )

    ground = Box(
        halfWidth=WIDTH/2,
        halfHeight=20,
        posX=0,
        posY=-HEIGHT/2,
        charge=0,
        mass=1
    )

    lWall = Box(
        halfWidth=20,
        halfHeight=HEIGHT//2,
        posX=-WIDTH//2,
        posY=0,
        charge=0,
        mass=1
    )

    rWall = Box(
        halfWidth=20,
        halfHeight=HEIGHT//2,
        posX=WIDTH//2,
        posY=0,
        charge=0,
        mass=1
    )

    roof = Box(
        halfWidth=WIDTH/2,
        halfHeight=20,
        posX=0,
        posY=HEIGHT/2,
        charge=0,
        mass=1
    )

    plat01 = Box(
        halfWidth=50,
        halfHeight=20,
        posX=-150,
        posY=-250,
        charge=0,
        mass=1
    )
    
    plat02 = Box(
        halfWidth=50,
        halfHeight=20,
        posX=34,
        posY=-137,
        charge=0,
        mass=1
    )

    plat03 = Box(
        halfWidth=50,
        halfHeight=20,
        posX=-100,
        posY=25,
        charge=0,
        mass=1
    )

    plat04 = Box(
        halfWidth=50,
        halfHeight=20,
        posX=150,
        posY=-25,
        charge=0,
        mass=1
    )


    blackHole1 = Particle(
        posX=-400, 
        posY=120, 
        charge=0, 
        mass=50000)
    blackHole2 = Particle(
        posX=400, 
        posY=120, 
        charge=0, 
        mass=50000)
    blackHole3 = Particle(
        posX=0, 
        posY=300, 
        charge=0, 
        mass=100000)


    globalField = (0,-10)

    renderer = Renderer(WIDTH, HEIGHT, 'jump')
    controlHandler = ControlHandler(player)

    clock = pygame.time.Clock()
    running = True

    rectList = [ground, lWall, rWall, roof, plat01, plat02, plat03, plat04, player]
    globalFieldList = [globalField]
    objectList = [player]
    staticObjectList = [ground, lWall, rWall, roof, plat01, plat02, plat03, plat04]
    fieldList = [blackHole1, blackHole2, blackHole3]
    timeDelta = 0.1
    envMod = 1

    sortedBoxList = []

    

    while running:

        #we build the sorted list of all absciss
        sortedBoxList = buildSortedBoxList(staticObjectList)

        #We resolve user inputs and game mecanic
        running = eventHandling(controlHandler)
        playerMovementLoop(player, sortedBoxList, timeDelta)

        #We execute the physic simulation
        physicLoop(
            player, sortedBoxList, 
            objectList, fieldList, 
            globalFieldList, timeDelta, 
            envMod)

        #We draw the result on the screen
        renderer.reset()
        renderer.drawCircle(blackHole1.getX(), blackHole1.getY(), 30)
        renderer.drawCircle(blackHole2.getX(), blackHole2.getY(), 30)
        renderer.drawCircle(blackHole3.getX(), blackHole3.getY(), 30)
        for rect in rectList:
            renderer.drawRect(
                rect.getX(), 
                rect.getY(), 
                rect.getHalfWidth(), 
                rect.getHalfHeight()
            )
        renderer.update()
        clock.tick(120)