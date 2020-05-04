from importer import *
from random import randrange
import math

if __name__ == "__main__":
    '''
    Simple script to test the gravity simulation
    '''
    

    ## Pygame init
    HEIGHT = 720
    WIDTH = 1080
    renderer = Renderer(WIDTH, HEIGHT, "Planet")
    clock = pygame.time.Clock()
    running = True

    #Physic init
    #Creation of our objects
    sun1 = Particle(
        posX=0, 
        posY=0, 
        charge=-1000, 
        mass=100000)
    sun2 = Particle(
        posX=250, 
        posY=-216, 
        charge=-1000, 
        mass=100000)
    sun3 = Particle(
        posX=0, 
        posY=216, 
        charge=-1000, 
        mass=100000)
        
    objectList = [
        Particle(
            randrange(-400,400), 
            randrange(-400,400),
            charge = 1,
            mass = randrange(50, 4000),
            speedX=0,
            speedY=0
        ) for i in range(15)]

    fieldList = [sun1]+objectList
    
    # Setting of the environment variables
    # timedelta sets the speed of the simulation
    timeDelta = 0.05
    # timedelta sets the strengh of gravity in the simulation
    envMod = 1
    
    while running:
        #print("=======================")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        loop(objectList, fieldList, [], timeDelta, envMod)

        renderer.reset()
        
        renderer.drawCircle(sun1.getX(), sun1.getY(), 10)
        # renderer.drawCircle(sun2.getX(), sun2.getY(), 10)
        # renderer.drawCircle(sun3.getX(), sun3.getY(), 10)

        for obj in objectList:
            renderer.drawCircle(
                obj.getX(), 
                obj.getY(), 
                int(30*obj.getMass()/4000), 
                (
                    int(200*obj.getMass()/4000), 
                    int(200*obj.getMass()/4000), 
                    int(200*obj.getMass()/4000)
                ))

        #print("=======================")

        renderer.update()
        clock.tick(120)

