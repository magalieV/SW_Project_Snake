"""Settings.py: File that handle global class"""

from game_module.gameplay.Enumerations import Movement, Turn
import pygame

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

SPRITE_SIZE = 20

class Grill:
    movement = Movement.UP
    x = 0
    y = 0
    tick = 0
    turn = Turn.NONE
    rect_value = None

    def __init__(self, mov, x, y, tick=0):
        self.movement = mov
        self.x = x
        self.y = y
        self.tick = tick

    def display_console(self):
        print("x = ", self.x, " and y = ", self.y, " and movement = ", self.movement, " turn = ", self.turn)

    def to_write_str(self):
        return str(self.movement.value) + "," + str(self.x) + "," + str(self.y) + "\n"

    def collide(self, position):
        element_rect = pygame.Rect(position[0], position[1], SPRITE_SIZE, SPRITE_SIZE)
        self.rect_value = pygame.Rect(self.x, self.y, SPRITE_SIZE, SPRITE_SIZE)
        if self.rect_value.colliderect(element_rect):
            return True
        return False

