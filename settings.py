import time

from button import Button


class Settings:
    def __init__(self, display):
        self.display = display

        # кнопки
        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Настройки и управление', 80)
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

        # управление
        self.controlsText = []
        self.controlsText.append(Button(display, 600, 500, 'assets/backgroundEmpty.png', 'WASD/стрелки - передвижение', 46))
        self.controlsText.append(Button(display, 600, 575, 'assets/backgroundEmpty.png', 'C - замедление времени (2 раза за уровень)', 46))
        self.controlsText.append(Button(display, 600, 650, 'assets/backgroundEmpty.png', 'V - неуязвимость (1 раз за уровень)', 46))
        self.controlsText.append(Button(display, 600, 725, 'assets/backgroundEmpty.png', 'Esc - пауза, Пробел - выход из паузы/начать уровень заново', 46))

        self.settingsData = open('assets/settings/settings.txt', 'r').readlines()
        self.difficulty = float(self.settingsData[0])

    def run(self):
        self.display.fill('black')

        self.label.draw()
        self.difficultyLabel.draw()
        self.returnButton.draw()

        for text in self.controlsText:
            text.draw()

        # смена сложности
        self.changedDifficulty -= 1
        for button in self.difficultyButtons:
            if button.pressed:
                button.pressed = False
                if self.changedDifficulty <= 0:
                    self.difficulty = (self.difficulty + 1) % len(self.difficultyButtons)
                    self.changedDifficulty = 30
                with open('assets/settings/settings.txt', 'w') as settings:
                    settings.writelines(str(self.difficulty))

        match self.difficulty:
            case 0:
                self.explorerDifficultyButton.draw()
                self.explorerDifficultyLabel.draw()
            case 1:
                self.easyDifficultyButton.draw()
                self.easyDifficultyLabel.draw()
            case 2:
                self.hardDifficultyButton.draw()
                self.hardDifficultyLabel.draw()

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'back'
