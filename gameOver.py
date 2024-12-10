# imports
import time
import webbrowser
from sounds import sounds
from button import Button


# class for GameOver state
class GameOver:
    def __init__(self, display):
        self.display = display

        # creating buttons
        self.restartButton = Button(display, 300, 400, 'assets/buttonBackgroundWhite.png', 'Заново')
        self.menuButton = Button(display, 900, 400, 'assets/buttonBackgroundWhite.png', 'Меню')
        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Игра окончена :(', 80, 'red')
        self.giveUpButton = Button(display, 600, 600, 'assets/buttonBackgroundWhite.png', 'Я сдаюсь(')

    # doing stuff
    def run(self):
        self.display.fill('black')

        # drawing buttons
        self.restartButton.draw()
        self.menuButton.draw()
        self.giveUpButton.draw()
        self.label.draw()

        # checking whether any buttons are pressed and changing game state if needed
        if self.restartButton.pressed:
            return 'level0'
            # self.gameStateManager.set_state('level')
        elif self.menuButton.pressed:
            return 'menu'
            # self.gameStateManager.set_state('menu')
        elif self.giveUpButton.pressed:
            webbrowser.open('https://rutube.ru/video/4481c5e861a22c5e2369a8ca10fd40c0/')
            sounds.play('giveUp')
            time.sleep(1)
