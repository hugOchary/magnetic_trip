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
        posX=-250, 
        posY=-216, 
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
            speedX=randrange(-30, 30),
            speedY=randrange(-30, 30)
        ) for i in range(100)]

    fieldList = [sun1, sun2, sun3]+objectList
    
    # Setting of the environment variables
    timeDelta = 0.1
    envMod = 1
    
    while running:
        #print("=======================")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        loop(objectList, objectList, [], timeDelta, envMod)

        renderer.reset()
        
        # renderer.drawCircle(sun1.getX(), sun1.getY(), 10)
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

