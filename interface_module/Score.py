"""score.py: File that handle the display of the score"""

import pygame

__author__ = "Irama Chaouch"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class ScoreGame:
    def __init__(self, window):
        self.score = 0
        self._window = window
        self.score_font = pygame.font.Font("menu_module/assets/Granjon.otf", 15)
        self.scoretext = self.score_font.render(
            f"Score : {str(self.score)}",
            False,
            (255, 255, 255)
        )

    def score_up(self):
        self.score += 1
        self.scoretext = self.score_font.render(
            f"Score : {str(self.score)}",
            False,
            (255, 255, 255)
        )

    def set_score(self, score):
        self.score = score
        self.scoretext = self.score_font.render(
            f"Score : {str(self.score)}",
            False,
            (255, 255, 255)
        )

    def display(self):
        self._window.blit(self.scoretext, [10, 0])
