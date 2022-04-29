"""Settings.py: File that handle global class"""

from Enumerations import Movement

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Grill:
    movement = Movement.UP
    x = 0
    y = 0
    tick = 0

    def __init__(self, mov, x, y, tick=0):
        self.movement = mov
        self.x = x
        self.y = y
        self.tick = tick

    def display_console(self):
        print("x = ", self.x, " and y = ", self.y, " and movement = ", self.movement)