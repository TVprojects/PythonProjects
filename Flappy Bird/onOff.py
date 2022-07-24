import pygame


class OnOff:
    def __init__(self, x, y):

        self.switch_red = pygame.image.load('afbeeldingen/switch_red.png').convert_alpha()
        self.switch_green = pygame.image.load('afbeeldingen/switch_green.png').convert_alpha()

        self.rect = self.switch_red.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface, state):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                state = not state

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if state:
            surface.blit(self.switch_green, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.switch_red, (self.rect.x, self.rect.y))

        return state

