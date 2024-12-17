# imports
from wall import Wall
from bat import Bat
from thorn import Thorn
from endPortal import EndPortal
from cannon import Cannon


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

                # misc
                # . - free space
                # E - end
                # W - wall

                # bats
                # V - vertical bat
                # H - horizontal bat

                # thorns
                # 1 - up thorns
                # 2 - right thorns
                # 3 - down thorns
                # 4 - left thorns

                # cannons
                # 5 - up cannon
                # 6 - right cannon
                # 7 - down cannon
                # 8 - left cannon
                
                x = j * 30
                y = i * 30
                match self.lines[i][j]:
                    case 'E':
                        result.append(EndPortal(self.display, x, y))
                    case 'W':
                        result.append(Wall(self.display, x, y))
                    case 'V':
                        result.append(Bat(self.display, x, y, 'vert', True))
                    case 'H':
                        result.append(Bat(self.display, x, y, 'hor', True))
                    case '1':
                        result.append(Thorn(self.display, x, y, 'South'))
                    case '2':
                        result.append(Thorn(self.display, x, y, 'West'))
                    case '3':
                        result.append(Thorn(self.display, x, y, 'North'))
                    case '4':
                        result.append(Thorn(self.display, x, y, 'East'))
                    case '5':
                        result.append(Cannon(self.display, x, y, 'North'))
                    case '6':
                        result.append(Cannon(self.display, x, y, 'East'))
                    case '7':
                        result.append(Cannon(self.display, x, y, 'South'))
                    case '8':
                        result.append(Cannon(self.display, x, y, 'West'))
                    case _:
                        pass
        return result
