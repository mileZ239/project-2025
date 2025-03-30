import pygame


class Star:
    def __init__(self, display, x, y):
        self.display = display

        self.x = x
        self.y = y

        self.sprite = pygame.image.load('assets/star.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'star'

        self.addTime = 60 * 10

    def delete(self):
        self.x = -239
        self.y = -239
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))

    def run(self):
        self.display.blit(self.sprite, self.rect)
