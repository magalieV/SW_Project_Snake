from __future__ import print_function, division
import pygame
from pygame.locals import *
from Map import Map


class Actions():

    done = False

    def __init__(self, width=1000, height=800):
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Generat Map")

        self.map = Map(self.screen)

    def main_actions(self):
        while not self.done:
            self.handle_events()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def draw(self):
        self.screen.fill(Color("gray20"))
        self.map.draw()
        pygame.display.flip()


if __name__ == "__main__":
    game = Actions()
    game.main_actions()
