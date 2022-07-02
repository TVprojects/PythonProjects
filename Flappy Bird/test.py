import pygame
import button

window_hoogte = 499
window_breedte = 600

screen = pygame.display.set_mode((window_breedte, window_hoogte))
pygame.display.set_caption('Button')

button_start = pygame.image.load('afbeeldingen/Flappy-start-button.png').convert_alpha()
button_rang = pygame.image.load('afbeeldingen/rang.png')


button_start = button.Button(158, 275, button_start, 1)
button_rang = button.Button(408, 275, button_rang, 1)

run = True
while run:
    screen.fill((202, 228, 241))
    if button_start.draw(screen):
        print("Play")
    if button_rang.draw(screen):
        print("Rang")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
