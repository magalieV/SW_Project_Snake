from curses import window
import pygame
from pygame.locals import *
from Interface import Interface


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
