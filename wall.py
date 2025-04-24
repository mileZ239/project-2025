import pygame


class Wall:
    def __init__(self, display, x, y):
        self.display = display
        self.x = x
        self.y = y
        self.sprite = pygame.image.load('assets/wall.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'wall'

    def run(self):
        self.display.blit(self.sprite, self.rect)
