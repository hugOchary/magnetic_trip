import pygame

#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT                left arrow
#K_BACKSPACE   \b      backspace
#K_TAB         \t      tab
#K_CLEAR               clear
#K_RETURN      \r      return
#K_PAUSE               pause
#K_ESCAPE      ^[      escape

class Controller:

    def __init__(self, player):
        self.player = player
    
    def handleDown(self, event):
        if event.key == pygame.K_LEFT:
            self.player.goLeft()
        elif event.key == pygame.K_RIGHT:
            self.player.goRight()
        elif event.key == pygame.K_SPACE:
            self.player.jump()

    def handleUp(self, event):
        if event.key == pygame.K_LEFT:
           self. player.stop(0)
        elif event.key == pygame.K_RIGHT:
            self.player.stop(1)
        else:
            pass