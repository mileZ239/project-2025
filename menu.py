# imports
import time
import pygame
import sys
from button import Button


# menu class
class Menu:
    def __init__(self, display):
        self.display = display

        # creating buttons
        self.startButton = Button(display, 600, 450, 'assets/buttonBackgroundWhite.png', 'Начать')
        self.exitButton = Button(display, 600, 650, 'assets/buttonBackgroundWhite.png', 'Выход')
        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Название игры', 80)
        self.settingsButton = Button(display, 1140, 60, 'assets/settingsButton.png')
        self.recordButton = Button(display, 60, 60, 'assets/trophyButton.png')

    # doing stuff
    def run(self):
        self.display.fill('black')

        # drawing buttons
        self.startButton.draw()
        self.exitButton.draw()
        self.label.draw()
        self.settingsButton.draw()
        self.recordButton.draw()

        # checking whether any buttons are pressed
        if self.startButton.pressed:
            time.sleep(0.3)
            # updating game state
            return 'chooseLevel'
        elif self.settingsButton.pressed:
            time.sleep(0.3)
            return 'settings'
        elif self.exitButton.pressed:
            pygame.quit()
            sys.exit()
        elif self.recordButton.pressed:
            return 'records'
