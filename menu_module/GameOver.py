"""GameOver.py: File that handle the display of the GameOver screen"""

"""Import statement go there"""

from pygame.locals import *
import pygame
from menu.Menu import *
from menu.MenuRedirection import MenuRedirection

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class GameOver:
    def __init__(self, window, window_size):
        self.window_size = window_size

        self.screen = window
        self._window_size = window_size

        self.background = pygame.image.load("menu/assets/background.jpg")
        self.font_btn = pygame.font.Font("menu/assets/Granjon.otf", 60)
        self.color_btn_text = (161, 144, 75)
        self.color_btn_bg = (8, 29, 30)
        self.color_btn_text_trigger = (113, 12, 26)
        self.sound_effect = pygame.mixer.Sound("game_module/assets/sound/over_sound.mp3")
        self.sound_effect.set_volume(0.7)
        self._back_size = (0.60 * window_size[0], 0.80 * window_size[1])

        self.text_game_over = self.font_btn.render(
            'GAME OVER', True, self.color_btn_text)
        self.text_to_menu = self.font_btn.render(
            'MENU', True, self.color_btn_text)
        self.text_quit = self.font_btn.render(
            'QUIT', True, self.color_btn_text)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self._rank_back = pygame.Surface((self._back_size[0], self._back_size[1]), pygame.SRCALPHA)
        self._rank_back.fill((0, 0, 0, 170))
        self._score = self.font_btn.render('0', False, (255, 40, 40))

    def set_score(self, score):
        self._score = self.font_btn.render(str(score), False, (255, 40, 40))

    def play_sound_effect(self):
        self.sound_effect.play()
        pygame.mixer.music.load("menu/assets/gameOver.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

    def init_rect(self):
        self.rect_to_menu = Rect((self._window_size[0] / 6) * 2 - (self.text_to_menu.get_width() / 2), (self._window_size[1] / 4) * 3, self.text_to_menu.get_width(), self.text_to_menu.get_height())
        self.rect_quit = Rect((self._window_size[0] / 6) * 4 - (self.text_quit.get_width() / 2), (self._window_size[1] / 4) * 3, self.text_quit.get_width(), self.text_quit.get_height())

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rect_quit, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rect_to_menu, 1)

    def draw_text(self):
        self.screen.blit(self._rank_back, (self._window_size[0]/2 - self._back_size[0]/2, 0.10 * self._window_size[1]))
        self.screen.blit(self.text_game_over, (self._window_size[0] / 2 - (self.text_game_over.get_width() / 2), self._window_size[1] / 4))
        self.screen.blit(self._score, (self._window_size[0] / 2 - (self._score.get_width() / 2), self._window_size[1] / 2))
        self.screen.blit(self.text_to_menu, ((self._window_size[0] / 6) * 2 - (self.text_to_menu.get_width() / 2), ((self._window_size[1] / 4) * 3)))
        self.screen.blit(self.text_quit, ((self._window_size[0] / 6) * 4 - (self.text_quit.get_width() / 2), ((self._window_size[1] / 4) * 3)))

    def collide_point(self, mouse):
        if Rect.collidepoint(self.rect_to_menu, mouse):
            self.text_to_menu = self.font_btn.render(
                'MENU', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rect_quit, mouse):
            self.text_quit = self.font_btn.render(
                'QUIT', True, self.color_btn_text_trigger)
        else:
            self.text_to_menu = self.font_btn.render(
                'MENU', True, self.color_btn_text)
            self.text_quit = self.font_btn.render(
                'QUIT', True, self.color_btn_text)

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Rect.collidepoint(self.rect_to_menu, mouse):
                    return MenuRedirection.MENU
                elif Rect.collidepoint(self.rect_quit, mouse):
                    return MenuRedirection.QUIT
            if event.type == pygame.QUIT:
                return MenuRedirection.QUIT
        return MenuRedirection.OVER

    def init(self):
        self.init_rect()
        self.draw_rect()

    def run_game_over(self):
        mouse = pygame.mouse.get_pos()
        self.screen.blit(self.background, (0, 0))

        self.draw_text()
        self.collide_point(mouse)
        return self.event_trigger(mouse)
