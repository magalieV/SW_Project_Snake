import pygame


class Interface:
    def __init__(self, _window: pygame.Surface):
        self.score = 0
        self.window = _window
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.scoretext = self.score_font.render(
            f"Score : {str(self.score)}",
            False,
            (235, 54, 229)
        )

    def score_up(self):
        self.score += 1
        self.scoretext = self.score_font.render(
            f"Score : {str(self.score)}",
            False,
            (235, 54, 229)
        )

    def set_score(self, score: int):
        self.score = score
        self.scoretext = self.score_font.render(
            f"Score : {str(self.score)}",
            False,
            (235, 54, 229)
        )

    def display(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.scoretext, [0, 0])
