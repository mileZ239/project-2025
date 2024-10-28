# imports
import pygame


# button class
class Button:
    def __init__(self, display, x, y, width, height, color, text=''):
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
                print("Button", self.text, "is pressed")
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
        self.display.blit(img, (rectCenterX - textCenterX, rectCenterY - textCenterY))
