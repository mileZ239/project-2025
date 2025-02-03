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
        self.sprites = {'East': pygame.image.load('assets/playerEast.png').convert(),
                        'West': pygame.image.load('assets/playerWest.png').convert(),
                        'South': pygame.image.load('assets/playerSouth.png').convert(),
                        'North': pygame.image.load('assets/playerNorth.png').convert(),
                        'Start': pygame.image.load('assets/playerSouth.png').convert()}
        self.spriteMoving = pygame.image.load('assets/playerMoving.png').convert()
        self.currentSprite = self.sprites['Start']
        self.rect = self.currentSprite.get_rect(center=(self.x + 15, self.y + 15))

        # something for colliding with walls
        self.ignoreX = -239
        self.ignoreY = -239

        # speed and moving state
        self.speedX = 0
        self.speedY = 0
        self.moving = False
        self.facing = 'Start'

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
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.facing != 'East':
            self.facing = 'East'
            self.ignoreX = -239
            self.ignoreY = self.y
            self.moving = True
            self.speedX = 15
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.facing != 'West':
            self.facing = 'West'
            self.ignoreX = -239
            self.ignoreY = self.y
            self.moving = True
            self.speedX = -15
        elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.facing != 'North':
            self.facing = 'North'
            self.ignoreX = self.x
            self.ignoreY = -239
            self.moving = True
            self.speedY = -15
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.facing != 'South':
            self.facing = 'South'
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
