from importer import *
import math

if __name__ == "__main__":
        
    

    ## Pygame init
    HEIGHT = 720
    WIDTH = 1080
    renderer = Renderer(WIDTH, HEIGHT, "Planet")
    clock = pygame.time.Clock()
    running = True

    # fireball = pygame.image.load('fireball.png').convert()
    # blackhole = pygame.image.load('blackHole.png').convert()

    #Physic init
    sun1 = Particle(
        posX=0, 
        posY=0, 
        charge=-1000, 
        mass=10000)
    sun2 = Particle(
        posX=-200, 
        posY=0, 
        charge=-1000, 
        mass=10000)
    planet = Particle(
        posX=100, 
        posY=0, 
        charge=1, 
        mass=100, 
        speedX=0,
        speedY=10)
    fieldList = [sun1, sun2]
    timeDelta = 0.1
    envMod = 1
    x0 = 0
    y0 = 0
    rad = 10000
    i=0

    # while i<rad and running:
    #     x1 = x0+math.sqrt(rad-i)
    #     x2 = x0-math.sqrt(rad-i)
    #     y1 = y0+math.sqrt(i)
    #     y2 = y0-math.sqrt(i)
    #     print("============ i = {0} ===============".format(i))
    #     print("Green : ",computeDistance(x1, y1, x0, x0))
    #     print("Blue : ",computeDistance(x1, y2, x0, x0))
    #     print("Red : ",computeDistance(x2, y1, x0, x0))
    #     print("Black : ",computeDistance(x2, y2, x0, x0))
    #     print("===========================")
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        planet.updateSpeed(
            computeNewObjSpeed(planet, fieldList, timeDelta, envMod)
        )

        planet.updatePos(
            computeNewObjPos(planet, timeDelta)
        )

        renderer.reset()


        
        # renderer.drawImage(blackHole, sun1.getX(), sun1.getY())
        # renderer.drawImage(blackHole, sun2.getX(), sun2.getY())
        # renderer.drawImage(fireball, planet.getX(), planet.getY())
        
        renderer.drawRect(sun1.getX(), sun1.getY(), 30, 30)
        renderer.drawRect(sun2.getX(), sun2.getY(), 30, 30)
        renderer.drawRect(planet.getX(), planet.getY(), 15, 15, (100, 100, 255))
        

        # renderer.drawRect(x0, y0, 15, 15)
        # renderer.drawRect(x1, y1, 15, 15, (0,255,0))
        # renderer.drawRect(x1, y2, 15, 15, (0,0,255))
        # renderer.drawRect(x2, y1, 15, 15, (255,0,0))
        # renderer.drawRect(x2, y2, 15, 15)

        renderer.update()
        i+=10
        clock.tick(120)

