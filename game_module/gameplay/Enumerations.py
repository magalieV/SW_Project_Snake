"""Enumerations.py: File that contain all enumeration of game part"""

from enum import Enum

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Movement(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class CollideType(Enum):
    BORDER = 1
    APPLE = 2
    NONE = 3


class Position(Enum):
    HORIZONTAL = 1
    VERTICAL = 2