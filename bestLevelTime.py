import time
from button import Button


class BestLevelTime:
    def __init__(self, display):
        self.display = display

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Лучшие прохождения', 80)
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')
        self.leftButton = Button(display, 1140, 700, 'assets/leftArrow.png')

        self.explorerDifficultyButton = Button(display, 1000, 300, 'assets/explorerDifficulty.png')
        self.easyDifficultyButton = Button(display, 1000, 300, 'assets/easyDifficulty.png')
        self.hardDifficultyButton = Button(display, 1000, 300, 'assets/hardDifficulty.png')

        self.difficultyButtons = [self.explorerDifficultyButton, self.easyDifficultyButton, self.hardDifficultyButton]
        self.changedDifficulty = 0
        self.difficulty = 0

        self.levelsCount = 2

        self.levelsTime = []
        self.levelsLabels = []
        for levelNumber in range(self.levelsCount):
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

            textExplorer = 'Уровень ' + str(levelNumber + 1) + ':          ' + str(timeExplorer) + ' с'
            if timeExplorer >= 10000:
                textExplorer = 'Уровень ' + str(levelNumber + 1) + ':          ' + 'не пройден :)'
            self.currentText.append(Button(display, 600, 300 + 70 * levelNumber, 'assets/buttonBackgroundBlack.png', textExplorer))

            textEasy = 'Уровень ' + str(levelNumber + 1) + ':          ' + str(timeEasy) + ' с'
            if timeEasy >= 10000:
                textEasy = 'Уровень ' + str(levelNumber + 1) + ':          ' + 'не пройден :)'
            self.currentText.append(Button(display, 600, 300 + 70 * levelNumber, 'assets/buttonBackgroundBlack.png', textEasy))

            textHard = 'Уровень ' + str(levelNumber + 1) + ':          ' + str(timeHard) + ' с'
            if timeHard >= 10000:
                textHard = 'Уровень ' + str(levelNumber + 1) + ':          ' + 'не пройден :)'
            self.currentText.append(Button(display, 600, 300 + 70 * levelNumber, 'assets/buttonBackgroundBlack.png', textHard))

            self.levelsLabels.append(self.currentText)

    def drawStuff(self):
        self.label.draw()
        self.returnButton.draw()
        self.leftButton.draw()

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
