# imports
import pygame
import sys
from button import Button


# menu class
class Menu:
    def __init__(self, display):
        self.display = display

        # creating buttons
        self.startButton = Button(display, 600, 450, 'assets/buttonBackgroundWhite.png', 'Начать', 48, pygame.Color(195, 2, 168))
        self.exitButton = Button(display, 600, 650, 'assets/buttonBackgroundWhite.png', 'Выход', 48, pygame.Color(195, 2, 168))
        self.gameButton = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Название игры', 80, pygame.Color(195, 2, 168))
        self.settingsButton = Button(display, 1140, 60, 'assets/settingsButton.png')

    # doing stuff
    def run(self):
        self.display.fill('black')

        # drawing buttons
        self.startButton.draw()
        self.exitButton.draw()
        self.gameButton.draw()
        self.settingsButton.draw()

        # checking whether any buttons are pressed
        if self.startButton.pressed:
            # updating game state
            return 'level'
            # self.gameStateManager.set_state('level')
        elif self.settingsButton.pressed:
            return 'settings'
        elif self.exitButton.pressed:
            pygame.quit()
            sys.exit()
