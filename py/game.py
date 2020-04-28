#!/usr/bin/env python3

import sys

import pygame
from graphicRenderer import GraphicRenderer
from physicObject import PhysicObject
from player import Player
from physicEngine import PhysicEngine
from controller import Controller


WIDTH = 1080
HEIGHT = 720

if __name__ == "__main__":

    ## Pygame init
    graphicRenderer = GraphicRenderer(1080, 720, 0, 0, "Magnetic trip")
    clock = pygame.time.Clock()
    running = True
    
    ## Game init
    objects = []
    ground = PhysicObject(50, WIDTH, HEIGHT, WIDTH/2, 0)
    plateform1 = PhysicObject(50, 200, HEIGHT-100, 100, 0)
    player = Player(50, 50, HEIGHT-250, WIDTH/2, 2, PhysicObject.DYNAMIC)
    statics = [ground, plateform1]
    dynamics = [player]
    controller = Controller(player)
    physicEngine = PhysicEngine()

    while running:

        ## Game engine

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                controller.handleDown(event)
            elif event.type == pygame.KEYUP:
                controller.handleUp(event)

        ## Physic engine
        physicEngine.loop(dynamics, statics)

        ## Graphic engine

        graphicRenderer.draw(statics+dynamics)
        graphicRenderer.update()

        clock.tick(60)
