import time

from button import Button


class Settings:
    def __init__(self, display):
        self.display = display

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Настройки', 80)
        self.difficultyLabel = Button(display, 350, 300, 'assets/buttonBackgroundBlack.png', 'Сложность', 60)
        self.easyDifficultyButton = Button(display, 800, 300, 'assets/easyDifficulty.png')
        self.hardDifficultyButton = Button(display, 800, 300, 'assets/hardDifficulty.png')
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')

        self.settingsData = open('assets/settings/settings.txt', 'r').readlines()
        self.difficulty = int(self.settingsData[0])

    def run(self):
        self.display.fill('black')

        self.label.draw()
        self.difficultyLabel.draw()
        self.returnButton.draw()

        if self.easyDifficultyButton.pressed or self.hardDifficultyButton.pressed:
            time.sleep(0.3)
            self.difficulty = 3 - self.difficulty
            with open('assets/settings/settings.txt', 'w') as settings:
                settings.writelines(str(self.difficulty))

        if self.difficulty == 1:
            self.easyDifficultyButton.draw()
        elif self.difficulty == 2:
            self.hardDifficultyButton.draw()

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'back'
