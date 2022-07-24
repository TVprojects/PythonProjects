import pygame


class Button:
    def __init__(self, x, y, image, scale):

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            action = self.clicked
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

