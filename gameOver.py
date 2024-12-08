# imports
import pygame
from button import Button


# class for GameOver state
class GameOver:
    def __init__(self, display):
        self.display = display

        # creating buttons
        self.restartButton = Button(display, 300, 400, 'assets/buttonBackgroundWhite.png', 'Заново', 48, pygame.Color(195, 2, 168))
        self.menuButton = Button(display, 900, 400, 'assets/buttonBackgroundWhite.png', 'Меню', 48, pygame.Color(195, 2, 168))
        self.text = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Игра окончена :(', 80, 'red')

    # doing stuff
    def run(self):
        self.display.fill('black')

        # drawing buttons
        self.restartButton.draw()
        self.menuButton.draw()
        self.text.draw()

        # checking whether any buttons are pressed and changing game state if needed
        if self.restartButton.pressed:
            return 'level'
            # self.gameStateManager.set_state('level')
        elif self.menuButton.pressed:
            return 'menu'
            # self.gameStateManager.set_state('menu')
