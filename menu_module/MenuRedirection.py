"""Menu.py: File that handle the display of the menu"""

from enum import Enum

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = ["Magalie Vandenbriele", "Irama Chaouch"]
__email__ = "magalie.vandenbriele@epitech.eu"


class MenuRedirection(Enum):
    MENU = 0
    PLAY = 1
    LOAD = 2
    RANKING = 3
    PAUSE = 4
    RESUME = 5
    RESTART = 6
    SAVE = 7
    QUIT = 8
    OVER = 9
    NONE = 10
    PLAY_MULTI = 11
    RESTART_MULTI = 12
    BOT = 13
