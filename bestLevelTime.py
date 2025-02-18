import time
from button import Button


class BestLevelTime:
    def __init__(self, display):
        self.display = display

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Лучшие прохождения', 80)
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')
        self.leftButton = Button(display, 1140, 700, 'assets/leftArrow.png')

        self.levelsTime = []
        self.levelsLabels = []
        for levelNumber in range(2):
            with open('assets/stats/levels/' + str(levelNumber) + '.txt', 'r') as levelStats:
                timee = round(float(levelStats.readlines()[0]) / 60, 2)
                levelStats.close()
            self.levelsTime.append(timee)

            text = 'Уровень ' + str(levelNumber) + ':          ' + str(timee) + ' с'
            if timee >= 10000:
                text = 'Уровень ' + str(levelNumber) + ':          ' + 'не пройден :)'
            self.levelsLabels.append(Button(display, 600, 300 + 70 * levelNumber, 'assets/buttonBackgroundBlack.png', text))

    def drawStuff(self):
        self.label.draw()
        self.returnButton.draw()
        self.leftButton.draw()
        for label in self.levelsLabels:
            label.draw()

    def run(self):
        self.display.fill('black')
        self.drawStuff()

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'menu'

        if self.leftButton.pressed:
            time.sleep(0.3)
            return 'back'
