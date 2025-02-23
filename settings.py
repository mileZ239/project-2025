import time

from button import Button


class Settings:
    def __init__(self, display):
        self.display = display

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Настройки', 80)
        self.difficultyLabel = Button(display, 350, 300, 'assets/buttonBackgroundBlack.png', 'Сложность', 60)
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')

        self.explorerDifficultyButton = Button(display, 800, 300, 'assets/explorerDifficulty.png')
        self.easyDifficultyButton = Button(display, 800, 300, 'assets/easyDifficulty.png')
        self.hardDifficultyButton = Button(display, 800, 300, 'assets/hardDifficulty.png')

        self.explorerDifficultyLabel = Button(display, 800, 400, 'assets/backgroundEmpty.png', 'Исследователь. Отключены большинство ловушек', 35, (81, 140, 158))
        self.easyDifficultyLabel = Button(display, 800, 400, 'assets/backgroundEmpty.png', 'Легко. Стандартная сложность', 35, (81, 140, 158))
        self.hardDifficultyLabel = Button(display, 800, 400, 'assets/backgroundEmpty.png', 'Сложно. Уменьшены интервалы времени у ловушек', 35, (81, 140, 158))

        self.difficultyButtons = [self.explorerDifficultyButton, self.easyDifficultyButton, self.hardDifficultyButton]
        self.changedDifficulty = 0

        self.settingsData = open('assets/settings/settings.txt', 'r').readlines()
        self.difficulty = float(self.settingsData[0])

    def run(self):
        self.display.fill('black')

        self.label.draw()
        self.difficultyLabel.draw()
        self.returnButton.draw()

        self.changedDifficulty -= 1
        for button in self.difficultyButtons:
            if button.pressed:
                button.pressed = False
                if self.changedDifficulty <= 0:
                    self.difficulty = (self.difficulty + 1) % len(self.difficultyButtons)
                    self.changedDifficulty = 30
                with open('assets/settings/settings.txt', 'w') as settings:
                    settings.writelines(str(self.difficulty))

        if self.difficulty == 0:
            self.explorerDifficultyButton.draw()
            self.explorerDifficultyLabel.draw()
        elif self.difficulty == 1:
            self.easyDifficultyButton.draw()
            self.easyDifficultyLabel.draw()
        elif self.difficulty == 2:
            self.hardDifficultyButton.draw()
            self.hardDifficultyLabel.draw()

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'back'
