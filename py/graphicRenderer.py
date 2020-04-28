import pygame
from pygame import Rect
from pygame.locals import *
from physicObject import PhysicObject

class GraphicRenderer:

    def __init__(self, width, height, xOrigin, yOrigin, title):
        self.width = width
        self.height = height
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin

        
        ## pygame init
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        pygame.mouse.set_visible(0)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
    
    def toRect(self, obj):
        halfWidth = obj.getHalfWidth()
        halfHeight = obj.getHalfHeight()
        return Rect(
            obj.getAbs()-halfWidth, 
            obj.getOrd()-halfHeight, 
            2*halfWidth, 
            2*halfHeight)

    def draw(self, objects):
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))
        
        for obj in objects:
            self.drawObject(obj)
        
        pygame.display.flip()
        

    def drawObject(self, obj):
        pygame.draw.rect(self.screen, (0,0,0), self.toRect(obj))
        
    def update(self):
        pygame.display.update()