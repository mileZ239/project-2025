# imports
from wall import Wall
from bat import Bat


# class for parsing data from .txt file
class LevelParser:
    def __init__(self, display, path):
        self.display = display
        self.path = path
        self.file = open(path, 'r')
        self.lines = self.file.readlines()

    def parse(self):
        # result array with walls and entities
        result = []

        for i in range(20):
            for j in range(30):
                # checking for wall / entity
                # W - wall
                # V - vertical bat
                # H - horizontal bat
                match self.lines[i][j]:
                    case 'W':
                        result.append(Wall(self.display, 'assets/wall.png', j * 30, i * 30))
                    case 'V':
                        result.append(Bat(self.display, 'assets/bat.png', j * 40, i * 40, 'vert', 200))
                    case 'H':
                        result.append(Bat(self.display, 'assets/bat.png', j * 40, i * 40, 'hor', 200))
                    case _:
                        pass
        return result
