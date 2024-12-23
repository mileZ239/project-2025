from button import Button


class Records:
    def __init__(self, display):
        self.display = display

        self.passesData = open('assets/playerData/passes.txt', 'r').readlines()
        self.deathsData = open('assets/playerData/deaths.txt', 'r').readlines()
        self.timeData = open('assets/playerData/time.txt', 'r').readlines()

        self.passes = int(self.passesData[0])
        self.deaths = int(self.deathsData[0])
        self.time = float(self.timeData[0]) / 60

        if self.passes == 0:
            self.avgDeaths = 0.0
            self.avgTime = 0.0
        else:
            self.avgDeaths = round(self.deaths / self.passes, 2)
            self.avgTime = round(self.time / self.passes, 2)

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Статистика', 80)
        self.avgDeathsLabel = Button(display, 600, 300, 'assets/buttonBackgroundBlack.png', 'В среднем смертей на уровень: ' + str(self.avgDeaths))
        self.avgTimeLabel = Button(display, 600, 400, 'assets/buttonBackgroundBlack.png', 'Среднее время прохождения уровня: ' + str(self.avgTime))
        self.allDeathsLabel = Button(display, 600, 500, 'assets/buttonBackgroundBlack.png', 'Всего смертей (анлак) : ' + str(self.deaths))

    def run(self):
        self.display.fill('black')

        self.label.draw()
        self.avgDeathsLabel.draw()
        self.avgTimeLabel.draw()
        self.allDeathsLabel.draw()