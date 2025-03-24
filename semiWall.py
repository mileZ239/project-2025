# imports
import pygame


# wall class
class SemiWall:
    def __init__(self, display, x, y):
        self.display = display
        self.x = x
        self.y = y
        self.sprite = pygame.image.load('assets/semiWall.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'semiWall'

    # doing stuff
    def run(self):
        self.display.blit(self.sprite, self.rect)
