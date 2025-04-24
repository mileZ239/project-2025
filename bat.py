import random
import pygame


class Bat:
    def __init__(self, display, x, y, direction, randomRange=False, flyingRange=100):
        self.display = display

        # начальные координаты
        self.baseX = x
        self.baseY = y

        # текущие координаты
        self.x = x
        self.y = y

        # скорость по осям
        self.speedX = 0
        self.speedY = 0
        if direction == 'hor':
            self.speedX = 5
        else:
            self.speedY = 5

        # рандомная длина полёта
        if randomRange:
            self.flyingRange = random.randint(flyingRange // 2, flyingRange * 3 // 2)
        else:
            self.flyingRange = flyingRange

        self.paused = 0
        self.sprite = pygame.image.load('assets/bat.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'bat'

    def run(self):
        # стоим или нет
        if self.paused > 0:
            self.paused -= 1
            self.display.blit(self.sprite, self.rect)
            return

        # движение
        self.x += self.speedX
        self.y += self.speedY
        if abs(self.x - self.baseX) + abs(self.y - self.baseY) >= self.flyingRange:
            self.speedX = -self.speedX
            self.speedY = -self.speedY

            # сколько кадров стоять
            self.paused = 30

        # рисование
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.display.blit(self.sprite, self.rect)
