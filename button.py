# imports
import pygame


# button class
class Button:
    def __init__(self, display, x, y, color, text='', fontSize=48, textColor='Purple'):
        self.display = display

        # position of the button
        self.x = x
        self.y = y

        # color of the button
        self.color = color

        # rectangle of the button
        self.sprite = pygame.image.load('assets/buttonBackgroundWhite.png')
        if color == 'black':
            self.sprite = pygame.image.load('assets/buttonBackgroundBlack.png')

        self.rect = self.sprite.get_rect()
        self.rect.center = (self.x, self.y)

        # button is pressed state
        self.pressed = False

        # button text
        self.text = text

        self.fontSize = fontSize
        self.textColor = textColor

    # doing stuff
    def draw(self):
        # getting current mouse position
        pos = pygame.mouse.get_pos()

        # checking whether button is pressed or not
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            self.pressed = True
            print("Button", self.text, "is pressed")
        else:
            self.pressed = False

        # drawing the button
        self.display.blit(self.sprite, self.rect)

        # initializing font
        font = pygame.font.SysFont(None, self.fontSize)
        img = font.render(self.text, True, self.textColor)

        # getting coordinates of the text
        textCenterX, textCenterY = img.get_rect().center
        rectCenterX, rectCenterY = self.x, self.y

        # updating the display
        self.display.blit(img, (rectCenterX - textCenterX, rectCenterY - textCenterY))
