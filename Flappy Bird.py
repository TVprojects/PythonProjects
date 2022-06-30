"""
Dit is Flappy Bird.
Een gebruiker drukt op SPATIE om de vogel te laten vliegen, anders valt de vogel naar beneden.
Als je door een pijp vliegt krijg je punten.
"""

import random
import sys
import pygame
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
grond = 0

def genereerPijp():
    offset = window_hoogte / 3
    pijp_hoogte = spel_afbeeldingen['pijp_afbeelding'][0].get_height()
    y2 = offset + random.randrange(0, int(window_hoogte - spel_afbeeldingen['grond'].get_height()- 1.2 * offset))
    x = window_breedte + 10
    y1 = pijp_hoogte - y2 + offset

    pijp = [
        # Boven pijp
        {'x': x, 'y': -y1},

        # Onder pijp
        {'x': x, 'y': y2},
    ]
    return pijp
def speel_flappybird():
    """""
    deze functie zorgt ervoor dat onze statische afbeeldingen met elkaar gaan communiceren en dat we daadwerkelijk
    het spel kunnen gaan spelen.
    """

    # Initialiseer een aantal variabelen
    score = 0
    mijn_hoogte = 100
    x = window_breedte // 5
    y = window_breedte // 2

    # Genereer 2 soorten pijpen. Deze noemen we onder pijpen en boven pijpen.
    eerste_pijp = genereerPijp()
    tweede_pijp = genereerPijp()

    print(eerste_pijp, tweede_pijp)

# Dit is de start van je programma
if __name__ == '__main__':
    # Initialiseer de pygame module
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
    spel_afbeeldingen['pijp_afbeelding'] = (pygame.transform.rotate(pygame.image.load(pijp_afbeelding).convert_alpha(), 180),
                                                                   pygame.image.load(pijp_afbeelding).convert_alpha())

    print("Welkom bij FlappyBird")
    print("Druk op SPATIE of ENTER om het spel te starten")

    # Game loop
    while True:

        # Zet bird op de juiste plek
        x = window_breedte // 5
        y = (window_hoogte - spel_afbeeldingen['flappybird'].get_height()) // 2

        while True:
            for evenement in pygame.event.get():

                # Een gebruiker kan het spel stoppen door op het kruisje te drukken of op ESC te drukken.
                if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.type == KSCAN_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # Als de gebruiker op spatie drukt, dan beweegt flappybird.
                elif evenement.type == KEYDOWN and (evenement.type == K_SPACE or evenement.key == K_SPACE):
                    speel_flappybird()

                # Als de gebruiker niets doet dan gebuird er ook niets.
                else:
                    window.blit(spel_afbeeldingen['achtergrond'], (0, 0))
                    window.blit(spel_afbeeldingen['flappybird'], (x, y))
                    window.blit(spel_afbeeldingen['grond'], (grond, verhoging))

                    pygame.display.update()
                    frames_per_seconden_klok.tick(frames_per_seconden)