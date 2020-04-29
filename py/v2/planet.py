from importer import *
import math

if __name__ == "__main__":
        
    

    ## Pygame init
    HEIGHT = 720
    WIDTH = 1080
    renderer = Renderer(WIDTH, HEIGHT, "Planet")
    clock = pygame.time.Clock()
    running = True

    #Physic init
    sun = Particle(0, 0, -1000, 10)
    planet = Particle(178, 274, 1, 0.1, 0, 0)
    fieldList = [sun]
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

        renderer.drawRect(planet.getX(), planet.getY(), 15, 15)
        renderer.drawRect(sun.getX(), sun.getY(), 30, 30)

        # renderer.drawRect(x0, y0, 15, 15)
        # renderer.drawRect(x1, y1, 15, 15, (0,255,0))
        # renderer.drawRect(x1, y2, 15, 15, (0,0,255))
        # renderer.drawRect(x2, y1, 15, 15, (255,0,0))
        # renderer.drawRect(x2, y2, 15, 15)

        renderer.update()
        i+=10
        clock.tick(120)

