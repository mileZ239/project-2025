class Stats:
    def __init__(self):
        self.passesData = open('assets/stats/passes.txt', 'r').readlines()
        self.deathsData = open('assets/stats/deaths.txt', 'r').readlines()
        self.timeData = open('assets/stats/time.txt', 'r').readlines()

        self.passes = int(self.passesData[0])
        self.deaths = int(self.deathsData[0])
        self.time = int(self.timeData[0])

    def updateDeaths(self, val):
        self.deaths += val
        with open('assets/stats/deaths.txt', 'w') as deaths:
            deaths.writelines(str(self.deaths))

    def updatePasses(self, val):
        self.passes += val
        with open('assets/stats/passes.txt', 'w') as passes:
            passes.writelines(str(self.passes))

    def updateTime(self, val):
        self.time += val
        with open('assets/stats/time.txt', 'w') as time:
            time.writelines(str(self.time))
