"""Menu.py: File that handle the display of the menu"""

"""Import statement go there"""




import sys
import pygame
from pygame.locals import *
def loadAndPlayMusic():
    pygame.mixer.music.load("assets/bg_music.mp3")
    pygame.mixer.music.play(-1)


def drawRect(screen, colorBtnBg, rectPlay, rectLoad, rectRanking, rectExit):
    pygame.draw.rect(screen, colorBtnBg, rectPlay, 1)
    pygame.draw.rect(screen, colorBtnBg, rectLoad, 1)
    pygame.draw.rect(screen, colorBtnBg, rectRanking, 1)
    pygame.draw.rect(screen, colorBtnBg, rectExit, 1)


def drawText(screen, textPlay, textLoad, textRanking, textExit, width):
    screen.blit(textPlay, (width/3 + 125, 120))
    screen.blit(textLoad, (width/3 + 125, 320))
    screen.blit(textRanking, (width/3, 520))
    screen.blit(textExit, (width/3 + 125, 720))


def start():
    pygame.init()
    pygame.mixer.init()
    running = True

    size = width, height = 1920, 1080

    screen = pygame.display.set_mode(size)

    background = pygame.image.load("assets/background.jpg")
    loadAndPlayMusic()
    fontBtn = pygame.font.Font("assets/Granjon.otf", 120)
    colorBtnText = (81, 73, 41)
    colorBtnBg = (8, 29, 30)
    colorBtnTextTrigger = (113, 12, 26)

    textPlay = fontBtn.render('PLAY', True, colorBtnText)
    textLoad = fontBtn.render('LOAD', True, colorBtnText)
    textRanking = fontBtn.render('RANKING', True, colorBtnText)
    textExit = fontBtn.render('EXIT', True, colorBtnText)

    width = screen.get_width()
    height = screen.get_height()

    while running:
        mouse = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        rectPlay = Rect(width/3 + 125, 120, 300, 150)
        rectLoad = Rect(width/3 + 125, 320, 300, 150)
        rectRanking = Rect(width/3, 520, 600, 150)
        rectExit = Rect(width/3 + 125, 720, 300, 150)

        drawRect(screen, colorBtnBg, rectPlay, rectLoad, rectRanking, rectExit)
        drawText(screen, textPlay, textLoad, textRanking, textExit, width)

        if Rect.collidepoint(rectPlay, mouse):
            textPlay = fontBtn.render('PLAY', True, colorBtnTextTrigger)
        elif Rect.collidepoint(rectLoad, mouse):
            textLoad = fontBtn.render('LOAD', True, colorBtnTextTrigger)
        elif Rect.collidepoint(rectRanking, mouse):
            textRanking = fontBtn.render('RANKING', True, colorBtnTextTrigger)
        elif Rect.collidepoint(rectExit, mouse):
            textExit = fontBtn.render('EXIT', True, colorBtnTextTrigger)
        else:
            textPlay = fontBtn.render('PLAY', True, colorBtnText)
            textLoad = fontBtn.render('LOAD', True, colorBtnText)
            textRanking = fontBtn.render('RANKING', True, colorBtnText)
            textExit = fontBtn.render('EXIT', True, colorBtnText)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                """provisional line, change it when you want to start the game developpement"""
                if Rect.collidepoint(rectExit, mouse) or Rect.collidepoint(rectLoad, mouse) or Rect.collidepoint(rectRanking, mouse) or Rect.collidepoint(rectPlay, mouse):
                    running = False
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    start()

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"
