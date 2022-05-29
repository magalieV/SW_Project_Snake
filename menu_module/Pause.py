"""Pause.py: File that handle the display of the pause menu"""

from menu_module.Menu import *
from pygame.locals import *
from menu_module.MenuRedirection import MenuRedirection
import pygame

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

BUTTON_IN_DIST = 40

class Pause:
    def __init__(self, window, window_size, button_distance=150, button_list_text=None):
        if button_list_text is None:
            button_list_text = [0, 1, 2, 3]

        self.window_size = window_size
        self.screen = window
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self._button_size = (350, 75)
        self.font_btn = pygame.font.Font("menu_module/assets/Granjon.otf", 60)
        self.color_btn_text = (161, 144, 75)
        self.color_btn_bg = (0, 0, 0)

        self._text = [self.font_btn.render('RESUME', True, self.color_btn_text),
                      self.font_btn.render('RESTART', True, self.color_btn_text),
                      self.font_btn.render('SAVE', True, self.color_btn_text),
                      self.font_btn.render('EXIT', True, self.color_btn_text)]

        self.button_distance = button_distance
        self.button_list_text = button_list_text


        self._play_rect = pygame.Surface((self._button_size[0], self._button_size[1]), pygame.SRCALPHA)
        self._play_rect.fill((30, 30, 30, 170))
        self._hover = MenuRedirection.NONE
        self._rect_hover = pygame.Surface((self._button_size[0], self._button_size[1]), pygame.SRCALPHA)
        self._rect_hover.fill((0, 0, 0, 255))

        self.rectangle = []

        separation = 0
        for index in range(0, len(self.button_list_text)):
            self.rectangle.append(Rect(self.width/3, separation + self.button_distance + (BUTTON_IN_DIST * index), self._button_size[0], self._button_size[1]))
            separation += 100

        self.redirection_list = [MenuRedirection.RESUME, MenuRedirection.RESTART, MenuRedirection.SAVE, MenuRedirection.MENU]


    def draw_rect(self, redirect, x, y):
        if self._hover is redirect:
            self.screen.blit(self._rect_hover, (x, y))
        else:
            self.screen.blit(self._play_rect, (x, y))

    def draw_button(self):
        idx = 0
        separation = 0
        for index in self.button_list_text:
            self.draw_rect(self.redirection_list[index], self.width/2 - self._button_size[0]/2, separation + self.button_distance + (BUTTON_IN_DIST * idx))
            separation += 100
            idx += 1

    def draw_text(self):
        separation = 5
        idx = 0
        for index in self.button_list_text:
            text = self._text[index]
            self.screen.blit(text, (self.width / 2 - text.get_width() / 2, separation + self.button_distance + (BUTTON_IN_DIST * idx)))
            separation += 100
            idx += 1

    def collide_point(self, mouse):
        idx = 0
        for index in self.button_list_text:
            if Rect.collidepoint(self.rectangle[idx], mouse):
                self._hover = self.redirection_list[index]
                return
            idx += 1
        self._hover = MenuRedirection.NONE

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                idx = 0
                for index in self.button_list_text:
                    if Rect.collidepoint(self.rectangle[idx], mouse):
                        return self.redirection_list[index]
                    idx += 1
            if event.type == pygame.QUIT:
                return MenuRedirection.QUIT
        return MenuRedirection.PAUSE

    def run_pause(self):
        mouse = pygame.mouse.get_pos()
        self.draw_button()
        self.draw_text()
        self.collide_point(mouse)
        return self.event_trigger(mouse)
