"""Menu.py: File that handle the display of the menu"""

from pygame.locals import *
import pygame
from menu_module.MenuRedirection import MenuRedirection

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = ["Magalie Vandenbriele", "Irama Chaouch"]
__email__ = "magalie.vandenbriele@epitech.eu"

BUTTON_DISTANCE = 150
BUTTON_IN_DIST = 40


class Menu:
    def __init__(self, window, window_size):
        self._window_size = window_size
        self._button_size = (500, 75)

        self.size = window_size[0], window_size[1]

        self.screen = window
        self._hover = MenuRedirection.NONE

        self.background = pygame.image.load(
            "menu_module/assets/background.jpg")
        self.font_btn = pygame.font.Font("menu_module/assets/Granjon.otf", 60)
        self.color_btn_text = (161, 144, 75)

        self.text_play = self.font_btn.render(
            'SINGLE PLAY', True, self.color_btn_text)
        self.text_play_two = self.font_btn.render(
            'DUAL PLAY', True, self.color_btn_text)
        self.text_load = self.font_btn.render(
            'LOAD', True, self.color_btn_text)
        self.text_ranking = self.font_btn.render(
            'RANKING', True, self.color_btn_text)
        self.text_exit = self.font_btn.render(
            'EXIT', True, self.color_btn_text)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self._play_rect = pygame.Surface(
            (self._button_size[0], self._button_size[1]), pygame.SRCALPHA)
        self._play_rect.fill((0, 0, 0, 170))

        self._rect_hover = pygame.Surface(
            (self._button_size[0], self._button_size[1]), pygame.SRCALPHA)
        self._rect_hover.fill((0, 0, 0, 255))

        self.rect_play = Rect(
            self.width/2 - self._button_size[0]/2, BUTTON_DISTANCE, self._button_size[0], self._button_size[1])
        self.rect_play_two = Rect(
            self.width/2 - self._button_size[0]/2, 80 + BUTTON_DISTANCE + BUTTON_IN_DIST, self._button_size[0], self._button_size[1])
        self.rect_load = Rect(self.width/2 - self._button_size[0]/2, 160 + BUTTON_DISTANCE + (
            BUTTON_IN_DIST * 2), self._button_size[0], self._button_size[1])
        self.rect_ranking = Rect(self.width/2 - self._button_size[0]/2, 240 + BUTTON_DISTANCE + (
            BUTTON_IN_DIST * 3), self._button_size[0], self._button_size[1])
        self.rect_exit = Rect(self.width/2 - self._button_size[0]/2, 320 + BUTTON_DISTANCE + (
            BUTTON_IN_DIST * 4), self._button_size[0], self._button_size[1])

    def load_and_play_music(self):
        pygame.mixer.music.load("menu_module/assets/ranking_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

    def draw_rect(self, redirect, x, y):
        if self._hover is redirect:
            self.screen.blit(self._rect_hover, (x, y))
        else:
            self.screen.blit(self._play_rect, (x, y))

    def draw_button(self):
        self.draw_rect(MenuRedirection.PLAY, self.width/2 -
                       self._button_size[0]/2, BUTTON_DISTANCE)
        self.draw_rect(MenuRedirection.PLAY_MULTI, self.width/2 -
                       self._button_size[0]/2, 80 + BUTTON_DISTANCE + BUTTON_IN_DIST)
        self.draw_rect(MenuRedirection.LOAD, self.width/2 -
                       self._button_size[0]/2, 160 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 2))
        self.draw_rect(MenuRedirection.RANKING, self.width/2 -
                       self._button_size[0]/2, 240 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 3))
        self.draw_rect(MenuRedirection.QUIT, self.width/2 -
                       self._button_size[0]/2, 320 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 4))

    def draw_text(self):
        self.screen.blit(self.text_play, (self.width/2 -
                         self.text_play.get_width() / 2, 5 + BUTTON_DISTANCE))
        self.screen.blit(self.text_play_two, (self.width/2 -
                         self.text_play_two.get_width() / 2, 85 + BUTTON_DISTANCE + BUTTON_IN_DIST))
        self.screen.blit(self.text_load, (self.width/2 - self.text_load.get_width() /
                         2, 165 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 2)))
        self.screen.blit(self.text_ranking, (self.width/2 - self.text_ranking.get_width() /
                         2, 245 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 3)))
        self.screen.blit(self.text_exit, (self.width/2 - self.text_exit.get_width() /
                         2, 325 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 4)))

    def collide_point(self, mouse):
        if Rect.collidepoint(self.rect_play, mouse):
            self._hover = MenuRedirection.PLAY
        elif Rect.collidepoint(self.rect_play_two, mouse):
            self._hover = MenuRedirection.PLAY_MULTI
        elif Rect.collidepoint(self.rect_load, mouse):
            self._hover = MenuRedirection.LOAD
        elif Rect.collidepoint(self.rect_ranking, mouse):
            self._hover = MenuRedirection.RANKING
        elif Rect.collidepoint(self.rect_exit, mouse):
            self._hover = MenuRedirection.QUIT
        else:
            self._hover = MenuRedirection.NONE

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Rect.collidepoint(self.rect_play, mouse):
                    return MenuRedirection.PLAY
                elif Rect.collidepoint(self.rect_play_two, mouse):
                    return MenuRedirection.PLAY_MULTI
                elif Rect.collidepoint(self.rect_load, mouse):
                    return MenuRedirection.LOAD
                elif Rect.collidepoint(self.rect_ranking, mouse):
                    return MenuRedirection.RANKING
                elif Rect.collidepoint(self.rect_exit, mouse):
                    return MenuRedirection.QUIT
            if event.type == pygame.QUIT:
                return MenuRedirection.QUIT
        return MenuRedirection.MENU

    def run_menu(self):
        mouse = pygame.mouse.get_pos()
        self.screen.blit(self.background, (0, 0))
        self.draw_button()
        self.draw_text()
        self.collide_point(mouse)
        return self.event_trigger(mouse)
