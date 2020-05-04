from importer import *

class ControlHandler():
    
    def __init__(self, player):
        self.player = player
    
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.handlePress(event)
        else:
            self.handleRelease(event)

    def handlePress(self, event):
        if event.key == pygame.K_LEFT:
            self.player.goDirection(-1)
        elif event.key == pygame.K_RIGHT:
            self.player.goDirection(1)
        elif event.key == pygame.K_SPACE:
            self.player.jump()
    
    def handleRelease(self, event):
        if event.key == pygame.K_LEFT:
            self.player.stopDirection(-1)
        elif event.key == pygame.K_RIGHT:
            self.player.stopDirection(1)