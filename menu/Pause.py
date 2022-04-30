"""Pause.py: File that handle the display of the pause menu"""

from Menu import *
from pygame.locals import *
import pygame
from enum import Enum

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Pause:
    def __init__(self):
        self.to_another_screen = MenuRedirection.PAUSE

        self.size = width, height = 990, 540

        self.screen = pygame.display.set_mode(self.size)

        self.font_btn = pygame.font.Font("assets/Granjon.otf", 60)
        self.color_btn_text = (81, 73, 41)
        self.color_btn_bg = (0, 0, 0)
        self.color_btn_text_trigger = (113, 12, 26)

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

    def init_rect(self):
        self.rectResume = Rect(self.width/3 + 62, 60, 250, 75)
        self.rectRestart = Rect(self.width/3 + 37, 160, 300, 75)
        self.rectSave = Rect(self.width/3 + 95, 260, 150, 75)
        self.rectExit = Rect(self.width/3 + 95, 360, 150, 75)

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectResume, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectRestart, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectSave, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectExit, 1)

    def draw_text(self):
        self.screen.blit(self.text_resume, (self.width/3 + 62, 60))
        self.screen.blit(self.text_restart, (self.width/3 + 37, 160))
        self.screen.blit(self.text_save, (self.width/3 + 95, 260))
        self.screen.blit(self.text_exit, (self.width/3 + 95, 360))

    def collide_point(self, mouse):
        if Rect.collidepoint(self.rectResume, mouse):
            self.text_resume = self.font_btn.render(
                'RESUME', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rectRestart, mouse):
            self.text_restart = self.font_btn.render(
                'RESTART', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rectSave, mouse):
            self.text_save = self.font_btn.render(
                'SAVE', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rectExit, mouse):
            self.text_exit = self.font_btn.render(
                'EXIT', True, self.color_btn_text_trigger)
        else:
            self.text_resume = self.font_btn.render(
                'RESUME', True, self.color_btn_text)
            self.text_restart = self.font_btn.render(
                'RESTART', True, self.color_btn_text)
            self.text_save = self.font_btn.render(
                'SAVE', True, self.color_btn_text)
            self.text_exit = self.font_btn.render(
                'EXIT', True, self.color_btn_text)

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Rect.collidepoint(self.rectResume, mouse):
                    return MenuRedirection.RESUME
                elif Rect.collidepoint(self.rectRestart, mouse):
                    return MenuRedirection.RESTART
                elif Rect.collidepoint(self.rectSave, mouse):
                    return MenuRedirection.SAVE
                elif Rect.collidepoint(self.rectExit, mouse):
                    return MenuRedirection.MENU
            if event.type == pygame.QUIT:
                pygame.quit()
        return self.to_another_screen

    def init(self):
        self.init_rect()
        self.draw_rect()

    def run_pause(self):
        mouse = pygame.mouse.get_pos()

        self.draw_text()
        self.collide_point(mouse)
        self.to_another_screen = self.event_trigger(mouse)
        if self.to_another_screen != MenuRedirection.PAUSE:
            return self.to_another_screen


def start_pause():
    pause = Pause()
    # add this function before the game loop
    pause.init()
    # add this function in the game loop
    pause.run_pause()
    #
    if pause.to_another_screen == MenuRedirection.RESTART:
        pygame.quit()
