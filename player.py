# imports
import pygame


# class for player
class Player:
    def __init__(self, display, x=0, y=0):
        self.display = display

        # position
        self.x = x
        self.y = y

        # sprites
        self.sprites = {'east': pygame.image.load('assets/playerEast.png').convert(),
                        'west': pygame.image.load('assets/playerWest.png').convert(),
                        'south': pygame.image.load('assets/playerSouth.png').convert(),
                        'north': pygame.image.load('assets/playerNorth.png').convert(),
                        'start': pygame.image.load('assets/playerSouth.png').convert()}
        self.spriteMoving = pygame.image.load('assets/playerMoving.png').convert()
        self.currentSprite = self.sprites['start']
        self.rect = self.currentSprite.get_rect(center=(self.x + 15, self.y + 15))

        # something for colliding with walls
        self.ignoreX = -239
        self.ignoreY = -239

        # speed and moving state
        self.speedX = 0
        self.speedY = 0
        self.moving = False
        self.facing = 'start'

        self.name = 'player'

    # movement
    def move(self):
        # moving
        self.x += self.speedX
        self.y += self.speedY

        # changing sprite
        if self.moving:
            self.currentSprite = self.spriteMoving
            return
        self.currentSprite = self.sprites[self.facing]

        # changing direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.facing != 'east':
            self.facing = 'east'
            self.ignoreX = -239
            self.ignoreY = self.y
            self.moving = True
            self.speedX = 15
        elif keys[pygame.K_a] and self.facing != 'west':
            self.facing = 'west'
            self.ignoreX = -239
            self.ignoreY = self.y
            self.moving = True
            self.speedX = -15
        elif keys[pygame.K_w] and self.facing != 'north':
            self.facing = 'north'
            self.ignoreX = self.x
            self.ignoreY = -239
            self.moving = True
            self.speedY = -15
        elif keys[pygame.K_s] and self.facing != 'south':
            self.facing = 'south'
            self.ignoreX = self.x
            self.ignoreY = -239
            self.moving = True
            self.speedY = 15
        else:
            self.moving = False
            self.ignoreX = -239
            self.ignoreY = -239

    # doing stuff
    def run(self):
        # moving the player
        self.move()
        self.rect = self.currentSprite.get_rect(center=(self.x + 15, self.y + 15))
        self.display.blit(self.currentSprite, self.rect)
