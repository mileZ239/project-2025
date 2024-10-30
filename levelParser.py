from wall import Wall


class LevelParser:
    def __init__(self, display, path):
        self.display = display
        self.path = path
        self.file = open(path, 'r')
        self.lines = self.file.readlines()

    def parse(self):
        result = []
        for i in range(20):
            for j in range(30):
                match self.lines[i][j]:
                    case '1':
                        result.append(Wall(self.display, 'assets/wallVertical.png', j * 40, i * 40))
                    case '2':
                        result.append(Wall(self.display, 'assets/wallHorizontal.png', j * 40, i * 40))
                    case _:
                        pass
        return result
