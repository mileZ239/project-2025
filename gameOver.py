import pygame

from button import Button


class GameOver:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.restartButton = Button(display, 300, 400, 'white', 'Заново', 48, pygame.Color(195, 2, 168))
        self.menuButton = Button(display, 900, 400, 'white', 'Меню', 48, pygame.Color(195, 2, 168))
        self.text = Button(display, 600, 100, 'black', 'Игра окончена :(', 80, 'red')

    def run(self):
        self.display.fill('black')
        self.restartButton.draw()
        self.menuButton.draw()
        self.text.draw()

        if self.restartButton.pressed:
            self.gameStateManager.set_state('level')
        if self.menuButton.pressed:
            self.gameStateManager.set_state('menu')
