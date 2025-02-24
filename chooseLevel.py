import time

from button import Button


class ChooseLevel:
    def __init__(self, display):
        self.display = display

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Выбор уровня', 80)
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')

        self.buttons = []
        for i in range(5):
            self.buttons.append(Button(display, 400, 250 + i * 150, 'assets/levelNotCompleted.png', f'Уровень {str(i + 1)}', 35))
        for i in range(5):
            self.buttons.append(Button(display, 800, 250 + i * 150, 'assets/levelNotCompleted.png', f'Уровень {str(i + 5)}', 35))

    def run(self):
        self.display.fill('black')

        self.label.draw()
        self.returnButton.draw()
        for button in self.buttons:
            button.draw()

        for i in range(8):
            if self.buttons[i].pressed:
                return 'level' + str(i)

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'back'
