import time
from button import Button


class BestLevelTime:
    def __init__(self, display):
        self.display = display

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Лучшие прохождения', 80)
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')
        self.leftButton = Button(display, 1140, 700, 'assets/leftArrow.png')

        self.explorerDifficultyButton = Button(display, 1100, 200, 'assets/explorerDifficulty.png')
        self.easyDifficultyButton = Button(display, 1100, 200, 'assets/easyDifficulty.png')
        self.hardDifficultyButton = Button(display, 1100, 200, 'assets/hardDifficulty.png')

        self.difficultyLabel = Button(display, 900, 200, 'assets/backgroundEmpty.png', 'Сложность: ')
        self.difficultyButtons = [self.explorerDifficultyButton, self.easyDifficultyButton, self.hardDifficultyButton]
        self.changedDifficulty = 0
        self.difficulty = 0

        self.levelsCount = 8

        # статистика по уровням
        self.levelsTime = []
        self.levelsLabels = []

        # читаем статистику
        for levelNumber in range(self.levelsCount):
            # читаем данные из файлов
            with open('assets/stats/levels/explorer/' + str(levelNumber) + '.txt', 'r') as levelStats:
                timeExplorer = round(float(levelStats.readlines()[0]) / 60, 2)
                levelStats.close()
            with open('assets/stats/levels/easy/' + str(levelNumber) + '.txt', 'r') as levelStats:
                timeEasy = round(float(levelStats.readlines()[0]) / 60, 2)
                levelStats.close()
            with open('assets/stats/levels/hard/' + str(levelNumber) + '.txt', 'r') as levelStats:
                timeHard = round(float(levelStats.readlines()[0]) / 60, 2)
                levelStats.close()
            self.levelsTime.append([timeExplorer, timeEasy, timeHard])

            self.currentText = []

            textX, textY = 300 + (levelNumber // 4) * 500, (levelNumber % 4) * 80 + 300

            # надписи
            textExplorer = 'Уровень ' + str(levelNumber + 1) + ':          ' + str(timeExplorer) + ' с'
            if timeExplorer >= 10000:
                textExplorer = 'Уровень ' + str(levelNumber + 1) + ':          ' + 'не пройден :('
            self.currentText.append(Button(display, textX, textY, 'assets/buttonBackgroundBlack.png', textExplorer, 45))

            textEasy = 'Уровень ' + str(levelNumber + 1) + ':          ' + str(timeEasy) + ' с'
            if timeEasy >= 10000:
                textEasy = 'Уровень ' + str(levelNumber + 1) + ':          ' + 'не пройден :('
            self.currentText.append(Button(display, textX, textY, 'assets/buttonBackgroundBlack.png', textEasy, 45))

            textHard = 'Уровень ' + str(levelNumber + 1) + ':          ' + str(timeHard) + ' с'
            if timeHard >= 10000:
                textHard = 'Уровень ' + str(levelNumber + 1) + ':          ' + 'не пройден :('
            self.currentText.append(Button(display, textX, textY, 'assets/buttonBackgroundBlack.png', textHard, 45))

            self.levelsLabels.append(self.currentText)

    def drawStuff(self):
        if self.difficulty == 0:
            self.label.textColor = (178, 194, 255)
        elif self.difficulty == 1:
            self.label.textColor = (163, 73, 164)
        elif self.difficulty == 2:
            self.label.textColor = (163, 0, 78)
        self.label.draw()
        self.returnButton.draw()
        self.leftButton.draw()
        self.difficultyLabel.draw()

        match self.difficulty:
            case 0:
                self.explorerDifficultyButton.draw()
            case 1:
                self.easyDifficultyButton.draw()
            case 2:
                self.hardDifficultyButton.draw()

        for i in range(self.levelsCount):
            self.levelsLabels[i][self.difficulty].draw()

    def run(self):
        self.display.fill('black')
        self.drawStuff()

        # смена сложности
        self.changedDifficulty -= 1
        for button in self.difficultyButtons:
            if button.pressed:
                button.pressed = False
                if self.changedDifficulty <= 0:
                    self.difficulty = (self.difficulty + 1) % len(self.difficultyButtons)
                    self.changedDifficulty = 30

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'menu'

        if self.leftButton.pressed:
            time.sleep(0.3)
            return 'back'
