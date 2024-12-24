import time

from button import Button


class Settings:
    def __init__(self, display):
        self.display = display
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')

    def run(self):
        self.display.fill('black')
        self.returnButton.draw()
        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'back'
