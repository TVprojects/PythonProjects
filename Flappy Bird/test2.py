import sys

import pygame
from pygame.locals import *
import onOff
import time

frames_per_seconden = 32
window_breedte = 600
window_hoogte = 499
window = pygame.display.set_mode((window_breedte, window_hoogte))

aanAf = onOff.OnOff(10, 10)
autoFly = False

while True:
    for evenement in pygame.event.get():
        # Een gebruiker kan het spel stoppen door op het kruisje te drukken of op ESC te drukken.
        if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.key == K_ESCAPE):
            print('QUIT')
            pygame.quit()
            sys.exit()

    autoFly = aanAf.draw(window, autoFly)
    pygame.display.update()


