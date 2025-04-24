class Stats:
    def __init__(self):
        # данные из файлов
        self.passesData = open('assets/stats/passes.txt', 'r').readlines()
        self.deathsData = open('assets/stats/deaths.txt', 'r').readlines()
        self.timeData = open('assets/stats/time.txt', 'r').readlines()

        self.passes = int(self.passesData[0])
        self.deaths = int(self.deathsData[0])
        self.time = int(self.timeData[0])

    def updateDeaths(self, val):
        with open('assets/stats/deaths.txt', 'r') as deaths:
            self.deaths = int(deaths.readlines()[0]) + val
            deaths.close()
        with open('assets/stats/deaths.txt', 'w') as deaths:
            deaths.writelines(str(self.deaths))
            deaths.close()

    def updatePasses(self, val):
        with open('assets/stats/passes.txt', 'r') as passes:
            self.passes = int(passes.readlines()[0]) + val
            passes.close()
        with open('assets/stats/passes.txt', 'w') as passes:
            passes.writelines(str(self.passes))
            passes.close()

    def updateTime(self, val):
        with open('assets/stats/time.txt', 'r') as timee:
            self.time = int(timee.readlines()[0]) + val
            timee.close()
        with open('assets/stats/time.txt', 'w') as timee:
            timee.writelines(str(self.time))
            timee.close()
