from curses import window
from matplotlib.pyplot import table
import pygame
from pygame.locals import *
from yaml import load
from Score import Interface

if __name__ == '__main__':

    (width, height) = (1000, 800)
    screen = pygame.display.set_mode((width, height))
    pygame.font.init()
    pygame.display.set_caption('Interface')
    running = True
    interface = Interface(screen)
    while running:
        interface.display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
