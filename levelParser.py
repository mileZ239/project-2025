from wall import Wall
from semiWall import SemiWall
from bat import Bat
from thorn import Thorn
from thornTrap import ThornTrap
from endPortal import EndPortal
from cannon import Cannon
from pufferfish import Pufferfish
from star import Star


# класс для парсинга .txt файлов в объекты уровней
class LevelParser:
    def __init__(self, display, path):
        self.display = display
        self.path = path
        self.file = open(path, 'r')
        self.lines = self.file.readlines()

    def parse(self):
        # итоговый массив с объектами
        result = []

        for i in range(27):
            for j in range(40):
                # проверка на сущность / стену

                # misc
                # . - free space
                # E - end
                # W - wall
                # w - semi wall
                # S - star

                # entities
                # V - vertical bat
                # H - horizontal bat
                # F - pufferfish

                # thorns
                # 1 - up thorns
                # 2 - right thorns
                # 3 - down thorns
                # 4 - left thorns

                # thorns trap
                # u - up thorns trap
                # r - right thorns trap
                # d - down thorns trap
                # l - left thorns trap

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
                    case 'w':
                        result.append(SemiWall(self.display, x, y))
                    case 'S':
                        result.append(Star(self.display, x, y))

                    case 'V':
                        result.append(Bat(self.display, x, y, 'vert', True))
                    case 'H':
                        result.append(Bat(self.display, x, y, 'hor', True))
                    case 'F':

                        result.append(Pufferfish(self.display, x, y))
                    case '1':
                        result.append(Thorn(self.display, x, y, 'South'))
                    case '2':
                        result.append(Thorn(self.display, x, y, 'West'))
                    case '3':
                        result.append(Thorn(self.display, x, y, 'North'))
                    case '4':
                        result.append(Thorn(self.display, x, y, 'East'))

                    case 'u':
                        result.append(ThornTrap(self.display, x, y, 'South'))
                    case 'r':
                        result.append(ThornTrap(self.display, x, y, 'West'))
                    case 'd':
                        result.append(ThornTrap(self.display, x, y, 'North'))
                    case 'l':
                        result.append(ThornTrap(self.display, x, y, 'East'))

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
