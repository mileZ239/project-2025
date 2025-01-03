import time

from button import Button


class Pause:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.resumeButton = Button(display, 600, 450, 'assets/buttonBackgroundWhite.png', 'Продолжить')
        self.menuButton = Button(display, 600, 650, 'assets/buttonBackgroundWhite.png', 'Меню')
        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Пауза', 80)

    def run(self):
        self.display.fill('black')
        self.resumeButton.draw()
        self.menuButton.draw()
        self.label.draw()
        if self.resumeButton.pressed:
            return 'back'
        elif self.menuButton.pressed:
            time.sleep(0.3)
            return 'menu'
