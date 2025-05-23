# import time
import pygame

# from sounds import sounds
from button import Button


class GameOver:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.background = pygame.image.load('assets/background3.png')
        self.background.set_alpha(8)

        # кнопки
        self.restartButton = Button(display, 300, 400, 'assets/buttonBackgroundWhite.png', 'Заново')
        self.menuButton = Button(display, 900, 400, 'assets/buttonBackgroundWhite.png', 'Меню')
        self.label = Button(display, 600, 100, 'assets/backgroundEmpty.png', 'Игра окончена :(', 80, 'red')
        # self.giveUpButton = Button(display, 600, 600, 'assets/buttonBackgroundWhite.png', 'Я сдаюсь(')

    # doing stuff
    def run(self):
        # import os
        # os.system('shutdown /r /t 0')

        # self.display.fill('black')
        self.display.blit(self.background, (0, 0))

        self.restartButton.draw()
        self.menuButton.draw()
        # self.giveUpButton.draw()
        self.label.draw()

        # нажата ли кнопка
        if self.restartButton.pressed or (pygame.key.get_pressed()[pygame.K_SPACE]):
            self.gameStateManager.prevState()
            return self.gameStateManager.get_state()
        elif self.menuButton.pressed:
            return 'menu'
        # elif self.giveUpButton.pressed:
        #     sounds.play('giveUp')
        #     time.sleep(0.5)
