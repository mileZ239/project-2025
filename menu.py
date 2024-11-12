# imports
import pygame
import sys
from button import Button


# menu class
class Menu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # creating buttons
        self.startButton = Button(display, 600, 450, 'gray', 'Начать', 48, pygame.Color(195, 2, 168))
        self.exitButton = Button(display, 600, 650, 'gray', 'Выйти', 48, pygame.Color(195, 2, 168))
        self.gameButton = Button(display, 600, 100, 'black', 'Название игры', 80, pygame.Color(195, 2, 168))

    # doing stuff
    def run(self):
        self.display.fill('black')

        # drawing buttons
        self.startButton.draw()
        self.exitButton.draw()
        self.gameButton.draw()

        # checking whether any buttons are pressed
        if self.startButton.pressed:
            # updating game state
            self.gameStateManager.set_state('level')
        if self.exitButton.pressed:
            pygame.quit()
            sys.exit()
