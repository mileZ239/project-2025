# imports
import pygame
import sys

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 30


# main class
class Game:
    def __init__(self):
        # initializing pygame
        pygame.init()

        # creating main display (surface)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # creating a clock for managing FPS
        self.clock = pygame.time.Clock()

        # creating an instance of GameStateManager class
        self.gameStateManager = GameStateManager('menu')

        # creating instances of Menu and Level classes
        self.menu = Menu(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)

        # creating a dictionary for our game states
        self.states = {'menu': self.menu, 'level': self.level}

    # main function
    def run(self):
        # main loop
        while True:
            # looking for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # running stuff at current state
            self.states[self.gameStateManager.get_state()].run()

            # updating display
            pygame.display.update()
            self.clock.tick(FPS)


# level class
class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    # doing stuff
    def run(self):
        self.display.fill('blue')


# menu class
class Menu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # creating buttons
        self.startButton = Button(display, 400, 400, 400, 75, 'gray', 'Начать')
        self.exitButton = Button(display, 400, 600, 400, 75, 'gray', 'Выйти')

    # doing stuff
    def run(self):
        self.display.fill('black')

        # drawing buttons
        self.startButton.draw()
        self.exitButton.draw()

        # checking whether any buttons are pressed
        if self.startButton.pressed:
            pass
        if self.exitButton.pressed:
            pygame.quit()
            sys.exit()


# class for managing game states
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    # getting current state
    def get_state(self):
        return self.currentState

    # setting state
    def set_state(self, state):
        self.currentState = state


# button class
class Button:
    def __init__(self, display, x, y, width, height, color, text=None):
        self.display = display

        # position of the button
        self.x = x
        self.y = y

        # width and height of the button
        self.width = width
        self.height = height

        # color of the button
        self.color = color

        # rectangle of the button
        self.rect = pygame.Rect((x, y), (width, height))

        # button is pressed state
        self.pressed = False

        # button text
        self.text = text

    # doing stuff
    def draw(self):
        # getting current mouse position
        pos = pygame.mouse.get_pos()

        # checking whether button is pressed or not
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False

        # drawing the button
        pygame.draw.rect(self.display, self.color, self.rect)

        # initializing font
        font = pygame.font.SysFont(None, 48)
        img = font.render(self.text, True, 'Purple')

        # getting coordinates of the text
        textCenterX, textCenterY = img.get_rect().center
        rectCenterX, rectCenterY = self.rect.center

        # updating the display
        self.display.blit(img, (textCenterX - rectCenterX, textCenterY - rectCenterY))


if __name__ == '__main__':
    # run the Game class
    game = Game()
    game.run()
