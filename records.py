import time
from button import Button


class Records:
    def __init__(self, display):
        self.display = display

        self.passesData = open('assets/stats/passes.txt', 'r').readlines()
        self.deathsData = open('assets/stats/deaths.txt', 'r').readlines()
        self.timeData = open('assets/stats/time.txt', 'r').readlines()

        self.passes = int(self.passesData[0])
        self.deaths = int(self.deathsData[0])
        self.time = float(self.timeData[0]) / 60

        if self.passes == 0:
            self.avgDeaths = 0.0
            self.avgTime = 0.0
        else:
            self.avgDeaths = round(self.deaths / self.passes, 2)
            self.avgTime = round(self.time / self.passes, 2)

        self.levelsCount = 8

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Статистика', 80)
        self.avgDeathsLabel = Button(display, 600, 300, 'assets/buttonBackgroundBlack.png', 'В среднем смертей на уровень: ' + str(self.avgDeaths))
        self.avgTimeLabel = Button(display, 600, 400, 'assets/buttonBackgroundBlack.png', 'Среднее время прохождения уровня: ' + str(self.avgTime) + ' с')
        self.allDeathsLabel = Button(display, 600, 500, 'assets/buttonBackgroundBlack.png', 'Всего смертей: ' + str(self.deaths))
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')
        self.resetButton = Button(display, 600, 700, 'assets/buttonBackgroundWhite.png', 'Сбросить статистику')
        self.rightButton = Button(display, 1140, 700, 'assets/rightArrow.png')

    def drawStuff(self):
        self.label.draw()
        self.avgDeathsLabel.draw()
        self.avgTimeLabel.draw()
        self.allDeathsLabel.draw()
        self.returnButton.draw()
        self.resetButton.draw()
        self.rightButton.draw()

    def reset(self):
        with open('assets/stats/deaths.txt', 'w') as deaths:
            deaths.writelines('0')
            deaths.close()
        with open('assets/stats/passes.txt', 'w') as passes:
            passes.writelines('0')
            passes.close()
        with open('assets/stats/time.txt', 'w') as timee:
            timee.writelines('0')
            timee.close()

        for i in range(self.levelsCount):
            with open(f'assets/stats/levels/explorer/{i}.txt', 'w') as levelStats:
                levelStats.writelines('10000000\n' + '-1\n')
                levelStats.close()
            with open(f'assets/stats/levels/easy/{i}.txt', 'w') as levelStats:
                levelStats.writelines('10000000\n' + '-1\n')
                levelStats.close()
            with open(f'assets/stats/levels/hard/{i}.txt', 'w') as levelStats:
                levelStats.writelines('10000000\n' + '-1\n')
                levelStats.close()

        for i in range(self.levelsCount):
            with open(f'assets/stats/levels/{i}.txt', 'w') as levelStats:
                levelStats.writelines('10000000\n' + '10000000\n')
                levelStats.close()

        time.sleep(0.3)

    def run(self):
        self.display.fill('black')
        self.drawStuff()

        if self.resetButton.pressed:
            self.reset()
            return 'back'

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'menu'

        if self.rightButton.pressed:
            time.sleep(0.3)
            return 'bestLevelTime'
