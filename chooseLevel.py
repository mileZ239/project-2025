import time

from button import Button


class ChooseLevel:
    def __init__(self, display):
        self.display = display

        self.label = Button(display, 600, 100, 'assets/buttonBackgroundBlack.png', 'Выбор уровня', 80)
        self.returnButton = Button(display, 1140, 60, 'assets/backArrow.png')

        self.levelsStars = []
        self.levelsCount = 8
        for i in range(self.levelsCount):
            with open(f'assets/stats/levels/explorer/{i}.txt') as levelStats:
                starsExplorer = int(levelStats.readlines()[1])
                levelStats.close()
            with open(f'assets/stats/levels/easy/{i}.txt') as levelStats:
                starsEasy = int(levelStats.readlines()[1])
                levelStats.close()
            with open(f'assets/stats/levels/hard/{i}.txt') as levelStats:
                starsHard = int(levelStats.readlines()[1])
                levelStats.close()
            self.levelsStars.append((starsExplorer, starsEasy, starsHard))

        self.difficulty = int(float(open('assets/settings/settings.txt', 'r').readlines()[0]))
        self.buttons = []
        for i in range(self.levelsCount // 2):
            stars = self.levelsStars[i][self.difficulty]
            if stars == -1:
                self.buttons.append(Button(display, 400, 250 + i * 150, 'assets/levelNotCompleted.png', f'Уровень {str(i + 1)}', 35))
            else:
                self.buttons.append(Button(display, 400, 250 + i * 150, f'assets/levelCompleted{stars}.png', f'Уровень {str(i + 1)}', 35))

        for i in range(self.levelsCount // 2, self.levelsCount):
            stars = self.levelsStars[i][self.difficulty]
            if stars == -1:
                self.buttons.append(Button(display, 800, 250 + (i - 4) * 150, 'assets/levelNotCompleted.png', f'Уровень {str(i + 1)}', 35))
            else:
                self.buttons.append(Button(display, 800, 250 + (i - 4) * 150, f'assets/levelCompleted{stars}.png', f'Уровень {str(i + 1)}', 35))

    def run(self):
        self.display.fill('black')

        self.label.draw()
        self.returnButton.draw()
        for button in self.buttons:
            button.draw()

        for i in range(self.levelsCount):
            if self.buttons[i].pressed:
                return 'level' + str(i)

        if self.returnButton.pressed:
            time.sleep(0.3)
            return 'back'
