import time
import pygame
import sys
from button import Button


class Menu:
    def __init__(self, display):
        self.display = display

        # кнопки
        self.startButton = Button(display, 600, 450, 'assets/buttonBackgroundWhite.png', 'Начать')
        self.exitButton = Button(display, 600, 650, 'assets/buttonBackgroundWhite.png', 'Выход')
        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Tomb of the Mask', 80)
        self.settingsButton = Button(display, 1140, 60, 'assets/settingsButton.png')
        self.recordButton = Button(display, 60, 60, 'assets/trophyButton.png')

        self.levelsCount = 8
        self.starsHard = 0

        # звёзды по сложностям
        for levelNumber in range(self.levelsCount):
            with open('assets/stats/levels/hard/' + str(levelNumber) + '.txt', 'r') as levelStats:
                stars = int(levelStats.readlines()[1])
                levelStats.close()
                self.starsHard += stars
        if self.starsHard == self.levelsCount * 3:
            self.label.textColor = pygame.Color(255, 246, 0)

    def run(self):
        self.display.fill('black')

        self.startButton.draw()
        self.exitButton.draw()
        self.label.draw()
        self.settingsButton.draw()
        self.recordButton.draw()

        # нажата ли какая-нибудь кнопка
        if self.startButton.pressed:
            time.sleep(0.3)
            return 'chooseLevel'
        elif self.settingsButton.pressed:
            time.sleep(0.3)
            return 'settings'
        elif self.exitButton.pressed:
            pygame.quit()
            sys.exit()
        elif self.recordButton.pressed:
            return 'records'
