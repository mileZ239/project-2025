# imports
from wall import Wall
from bat import Bat
from thorn import Thorn
from endPortal import EndPortal


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
                # . - free space
                # E - end
                # W - wall
                # V - vertical bat
                # H - horizontal bat
                # 1 - up thorns
                # 2 - right thorns
                # 3 - down thorns
                # 4 - left thorns
                match self.lines[i][j]:
                    case 'E':
                        result.append(EndPortal(self.display, j * 30, i * 30))
                    case 'W':
                        result.append(Wall(self.display, j * 30, i * 30))
                    case 'V':
                        result.append(Bat(self.display, j * 30, i * 30, 'vert', True))
                    case 'H':
                        result.append(Bat(self.display, j * 30, i * 30, 'hor', True))
                    case '1':
                        result.append(Thorn(self.display, j * 30, i * 30, 'South'))
                    case '2':
                        result.append(Thorn(self.display, j * 30, i * 30, 'West'))
                    case '3':
                        result.append(Thorn(self.display, j * 30, i * 30, 'North'))
                    case '4':
                        result.append(Thorn(self.display, j * 30, i * 30, 'East'))
                    case _:
                        pass
        return result
