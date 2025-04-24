import pygame


class Button:
    def __init__(self, display, x, y, background, text='', fontSize=48, textColor=pygame.Color(195, 2, 168)):
        self.display = display

        self.x = x
        self.y = y

        self.sprite = pygame.image.load(background)

        self.rect = self.sprite.get_rect()
        self.rect.center = (self.x, self.y)

        self.pressed = False

        self.text = text

        self.fontSize = fontSize
        self.textColor = textColor

    # doing stuff
    def draw(self):
        pos = pygame.mouse.get_pos()

        # проверяем нажата кнопка или нет
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            self.pressed = True
            # print("Button", self.text, "is pressed")
        else:
            self.pressed = False

        self.display.blit(self.sprite, self.rect)

        font = pygame.font.SysFont(None, self.fontSize)
        img = font.render(self.text, True, self.textColor)

        # координаты кнопки
        textCenterX, textCenterY = img.get_rect().center
        rectCenterX, rectCenterY = self.x, self.y

        self.display.blit(img, (rectCenterX - textCenterX, rectCenterY - textCenterY))
