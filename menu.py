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
        self.startButton = Button(display, 400, 400, 400, 75, 'gray', 'Начать')
        self.exitButton = Button(display, 400, 600, 400, 75, 'gray', 'Выйти')

    # doing stuff
    def run(self):
        self.display.fill('black')

        # drawing buttons
        self.startButton.draw()
        self.exitButton.draw()

        # checking whether any buttons are pressed
        if self.startButton.pressed:
            # updating game state
            self.gameStateManager.set_state('level')
        if self.exitButton.pressed:
            pygame.quit()
            sys.exit()
