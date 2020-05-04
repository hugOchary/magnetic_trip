import pygame
from pygame import Rect
from pygame.locals import *

class Renderer:

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = self.createScreen()
        pygame.display.set_caption(title)
        pygame.mouse.set_visible(0)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
    
    def createScreen(self):
        return pygame.display.set_mode((self.width, self.height))

    def pygameInit(self, title):
        pygame.init()
        self.screen = self.createScreen()
        pygame.display.set_caption(title)
        pygame.mouse.set_visible(0)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def toRect(self, objX, objY, halfWidth, halfHeight):
        return Rect(
            objX-halfWidth, 
            objY-halfHeight, 
            2*halfWidth, 
            2*halfHeight)
    
    def convertY(self, y):
        return self.height-y
    
    def centerX(self, x):
        return x + self.width/2
    
    def centerY(self,y):
        return y + self.height/2

    def drawRect(self, objX, objY, halfWidth, halfHeight, color = (0,0,0)):
        pygame.draw.rect(
            self.screen, 
            color,
            self.toRect( 
                self.centerX(objX), 
                self.convertY(self.centerY(objY)), 
                halfWidth, 
                halfHeight)
            )

    def drawCircle(self, objX, objY, radius, color = (0,0,0)):
        pygame.draw.circle(
            self.screen, 
            color, 
            (
                int(round(self.centerX(objX))), 
                int(round(self.convertY(self.centerY(objY))))
            ), 
            radius)

    def drawImage(self, image, objX, objY):
        self.screen.blit(image, (objX, objY))
    
    def reset(self):
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))

    def update(self):
        pygame.display.update()