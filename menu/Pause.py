"""Pause.py: File that handle the display of the pause menu"""

from menu.Menu import *
from pygame.locals import *
from menu.MenuRedirection import MenuRedirection
import pygame

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

BUTTON_DISTANCE = 130
BUTTON_IN_DIST = 40

class Pause:
    def __init__(self, window, window_size):
        self.window_size = window_size

        self.screen = window
        self._button_size = (350, 75)
        self.font_btn = pygame.font.Font("menu/assets/Granjon.otf", 60)
        self.color_btn_text = (161, 144, 75)
        self.color_btn_bg = (0, 0, 0)

        self._rect_trigger = (65, 255, 255, 45)
        self.text_resume = self.font_btn.render(
            'RESUME', True, self.color_btn_text)
        self.text_restart = self.font_btn.render(
            'RESTART', True, self.color_btn_text)
        self.text_save = self.font_btn.render(
            'SAVE', True, self.color_btn_text)
        self.text_exit = self.font_btn.render(
            'EXIT', True, self.color_btn_text)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self._play_rect = pygame.Surface((self._button_size[0], self._button_size[1]), pygame.SRCALPHA)
        self._play_rect.fill((100, 100, 100, 170))
        self._hover = MenuRedirection.NONE
        self._rect_hover = pygame.Surface((self._button_size[0], self._button_size[1]), pygame.SRCALPHA)
        self._rect_hover.fill((120, 120, 120, 255))

        self.rect_resume = Rect(self.width/3 + 62, BUTTON_DISTANCE, self._button_size[0], self._button_size[1])
        self.rect_restart = Rect(self.width/3 + 62, 100 + BUTTON_DISTANCE + BUTTON_IN_DIST, self._button_size[0], self._button_size[1])
        self.rect_save = Rect(self.width/3, 200 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 2), self._button_size[0], self._button_size[1])
        self.rect_quit = Rect(self.width/3 + 62, 300 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 3), self._button_size[0], self._button_size[1])

    def draw_rect(self, redirect, x, y):
        if self._hover is redirect:
            self.screen.blit(self._rect_hover, (x, y))
        else:
            self.screen.blit(self._play_rect, (x, y))

    def draw_button(self):
        self.draw_rect(MenuRedirection.RESUME, self.width/2 - self._button_size[0]/2, BUTTON_DISTANCE)
        self.draw_rect(MenuRedirection.RESTART, self.width/2 - self._button_size[0]/2, 100 + BUTTON_DISTANCE + BUTTON_IN_DIST)
        self.draw_rect(MenuRedirection.SAVE, self.width/2 - self._button_size[0]/2, 200 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 2))
        self.draw_rect(MenuRedirection.QUIT, self.width/2 - self._button_size[0]/2, 300 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 3))

    def draw_text(self):
        self.screen.blit(self.text_resume, (self.width / 2 - self.text_resume.get_width() / 2, 5 + BUTTON_DISTANCE))
        self.screen.blit(self.text_restart,(self.width / 2 - self.text_restart.get_width() / 2, 105 + BUTTON_DISTANCE + BUTTON_IN_DIST))
        self.screen.blit(self.text_save, (self.width / 2 - self.text_save.get_width() / 2, 205 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 2)))
        self.screen.blit(self.text_exit, (self.width / 2 - self.text_exit.get_width() / 2, 305 + BUTTON_DISTANCE + (BUTTON_IN_DIST * 3)))

    def collide_point(self, mouse):
        if Rect.collidepoint(self.rect_resume, mouse):
            self._hover = MenuRedirection.RESUME
        elif Rect.collidepoint(self.rect_restart, mouse):
            self._hover = MenuRedirection.RESTART
        elif Rect.collidepoint(self.rect_save, mouse):
            self._hover = MenuRedirection.SAVE
        elif Rect.collidepoint(self.rect_quit, mouse):
            self._hover = MenuRedirection.QUIT
        else:
            self._hover = MenuRedirection.NONE

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Rect.collidepoint(self.rect_resume, mouse):
                    return MenuRedirection.RESUME
                elif Rect.collidepoint(self.rect_restart, mouse):
                    return MenuRedirection.RESTART
                elif Rect.collidepoint(self.rect_save, mouse):
                    return MenuRedirection.SAVE
                elif Rect.collidepoint(self.rect_quit, mouse):
                    return MenuRedirection.MENU
            if event.type == pygame.QUIT:
                return MenuRedirection.QUIT
        return MenuRedirection.PAUSE

    def run_pause(self):
        mouse = pygame.mouse.get_pos()
        self.draw_button()
        self.draw_text()
        self.collide_point(mouse)
        return self.event_trigger(mouse)
