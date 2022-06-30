"""
Dit is Flappy Bird.
Een gebruiker drukt op SPATIE om de vogel te laten vliegen, anders valt de vogel naar beneden.
Als je door een pijp vliegt krijg je punten.
"""

import random
import sys
import pygame
import pygame as pygame
from pygame.locals import *

# Bepaal de hoogte van je speelscherm
window_breedte = 600
window_hoogte = 499

# Configutatie van het spel
window = pygame.display.set_mode((window_breedte, window_hoogte))
verhoging = window_hoogte * 0.8
spel_afbeeldingen = {}
frames_per_seconden = 32
pijp_afbeelding = 'afbeeldingen/pijp.png'
achtergrond_afbeelding = 'afbeeldingen/achtergrond.jpg'
vogel_afbeelding = 'afbeeldingen/vogel.png'
grond_afbeelding = 'afbeeldingen/grond.jfif'

# Dit is de start van je programma
if __name__ == '__main__':
    # Inistailseer de pygame module
    pygame.init()
    frames_per_seconden_klok = pygame.time.Clock()

    # Zet een titel voor de applicatie
    pygame.display.set_caption('Flappy Bird')

    # Laat alle afbeeldingen in.
    spel_afbeeldingen['score_afbeeldingen'] = (
        pygame.image.load('afbeeldingen/0.png').convert_alpha(),
        pygame.image.load('afbeeldingen/1.png').convert_alpha(),
        pygame.image.load('afbeeldingen/2.png').convert_alpha(),
        pygame.image.load('afbeeldingen/3.png').convert_alpha(),
        pygame.image.load('afbeeldingen/4.png').convert_alpha(),
        pygame.image.load('afbeeldingen/5.png').convert_alpha(),
        pygame.image.load('afbeeldingen/6.png').convert_alpha(),
        pygame.image.load('afbeeldingen/7.png').convert_alpha(),
        pygame.image.load('afbeeldingen/8.png').convert_alpha(),
        pygame.image.load('afbeeldingen/9.png').convert_alpha()
    )
    spel_afbeeldingen['flappybird'] = pygame.image.load(vogel_afbeelding).convert_alpha()
    spel_afbeeldingen['grond'] = pygame.image.load(grond_afbeelding).convert_alpha()
    spel_afbeeldingen['achtergrond'] = pygame.image.load(achtergrond_afbeelding).convert_alpha()
    spel_afbeeldingen['pijpafbeelding'] = (pygame.transform.rotate(pygame.image.load(pijp_afbeelding).convert_alpha(), 180),
                                                                   pygame.image.load(pijp_afbeelding).convert_alpha())

    print("Welkom bij FlappyBird")
    print("Druk op SPATIE of ENTER om het spel te starten")

    # Game loop
    while True:

        # Zet bird op de juiste plek
        x = window_breedte // 5
