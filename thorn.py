import pygame


class Thorn:
    def __init__(self, display, x, y, direction):
        self.display = display

        self.x = x
        self.y = y

        self.facing = direction
        self.sprite = pygame.image.load('assets/thorns' + direction + '.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'thorn'

    def run(self):
        self.display.blit(self.sprite, self.rect)
