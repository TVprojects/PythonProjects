"""
Dit is Flappy Bird.
Een gebruiker drukt op SPATIE om de vogel te laten vliegen, anders valt de vogel naar beneden.
Als je door een pijp vliegt krijg je punten.
"""

import random
import sys
import pygame
from pygame.locals import *
import button

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
start_afbeelding = 'afbeeldingen/flappy-bird-startscherm.jpg'
dood_afbeelding = 'afbeeldingen/dood_scherm.png'
start_img = pygame.image.load('afbeeldingen/Flappy-start-button.png').convert_alpha()
rang_img = pygame.image.load('afbeeldingen/rang.png')
grond = 0
playButtonPressed = False
rangButtonPressed = False

def genereerPijp():
    offset = window_hoogte / 3
    pijp_hoogte = spel_afbeeldingen['pijp_afbeelding'][0].get_height()
    y2 = offset + random.randrange(0, int(window_hoogte - spel_afbeeldingen['grond'].get_height() - 1.2 * offset))
    x = window_breedte + 10
    y1 = pijp_hoogte - y2 + offset

    pijp = [
        # Boven pijp
        {'x': x, 'y': -y1},

        # Onder pijp
        {'x': x, 'y': y2},
    ]
    return pijp

def is_dood(x, y, boven_pijpen, onder_pijpen):
    pijphoogte = spel_afbeeldingen['pijp_afbeelding'][0].get_height()
    pijpbreedte = spel_afbeeldingen['pijp_afbeelding'][0].get_width()

    # Valt de vogel op de grond / plafon?
    if y > verhoging - 25 or y < 0:
        return True

    # Komt de vogel tegen de bovenkant / bovenkant van de pijp?
    for pijp in boven_pijpen:

        if y < pijphoogte + pijp['y'] and abs(x - pijp['x']) < pijpbreedte:
            print("Dood van boven!")
            return True
    # Komt de vogel tegen de onderkant / onderkant van de pijp?
    for pijp in onder_pijpen:
        if y + spel_afbeeldingen['flappybird'].get_height() > pijp['y'] and abs(x - pijp['x']) < pijpbreedte:
            print("Dood van onder!")
            return True
    return False


def speel_flappybird():
    pop_start_scherm = 0
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

    # Genereer de boven en onder pijpen.
    onder_pijpen = [
        {'x': window_breedte + 300 - mijn_hoogte,
         'y': eerste_pijp[1]['y']},
        {'x': window_breedte + 300 - mijn_hoogte + (window_breedte / 2),
         'y': tweede_pijp[1]['y']}
    ]

    boven_pijpen = [
        {'x': window_breedte + 300 - mijn_hoogte,
         'y': eerste_pijp[0]['y']},
        {'x': window_breedte + 300 - mijn_hoogte + (window_breedte / 2),
        'y': tweede_pijp[0]['y']}
    ]

    # Hoe snel de vogel vliegt
    vogel_snelheid = -9
    vogel_maxsnelheid = 10
    vogel_toename_snelheid = 1
    vogel_falp_snelheid = -8
    vogelflapt = False

    while True:

        for evenement in pygame.event.get():
            # Een gebruiker kan het spel stoppen door op het kruisje te drukken of op ESC te drukken.
            if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.type == KSCAN_ESCAPE):
                pygame.quit()
                sys.exit()

            # Als de gebruiker op spatie drukt, dan beweegt flappybird.
            elif evenement.type == KEYDOWN and (evenement.type == K_SPACE or evenement.key == K_SPACE):

                if y > 0:
                    if pop_start_scherm == 0:

                        pop_start_scherm += 1
                    vogel_snelheid = vogel_falp_snelheid
                    vogelflapt = True

        if is_dood(x, y, boven_pijpen, onder_pijpen):
            return

        # Bepaal waar de speler zich bevindt.
        speler_midden_pos = x + spel_afbeeldingen['flappybird'].get_width() / 2

        # Bepaal waar de pijpen zich bevinden.
        for pijp in boven_pijpen:
            pijp_midden_pos = pijp['x'] + spel_afbeeldingen['pijp_afbeelding'][0].get_width() / 2

            # Als je voorbij zo een pijp komt, krijg je een punt.
            if pijp_midden_pos <= speler_midden_pos < pijp_midden_pos + 4:
                score += 1
                print(f"Je score is nu {score}!")

        # Als de gebruiker de vogel niet laat vliegen dan valt hij steeds harder naar benenden.
        if vogel_snelheid < vogel_maxsnelheid and not vogelflapt:
            vogel_snelheid += vogel_toename_snelheid
        if vogelflapt:
            vogelflapt = False

        # Bepaal de hoogte van de vogel wanneer iemand op spatie drukt.
        y = y + min(vogel_snelheid, verhoging - y - spel_afbeeldingen['flappybird'].get_height())

        # Verplaats de pijpen.
        for bovenpijp, onderpijp in zip(boven_pijpen, onder_pijpen):
            bovenpijp['x'] += -4
            onderpijp['x'] += -4

        # Genereer steeds nieuwe pijpen wanneer ze van het scherm zijn.
        if 0 < boven_pijpen[0]['x'] < 5:
            nieuwe_pijp = genereerPijp()
            boven_pijpen.append(nieuwe_pijp[0])
            onder_pijpen.append(nieuwe_pijp[1])

        # Als een pijp uit scherm verdwenen is, haal deze dan uit de lijst.
        if boven_pijpen[0]['x'] < -spel_afbeeldingen['pijp_afbeelding'][0].get_width():
            boven_pijpen.pop(0)
            onder_pijpen.pop(0)

        # Update alle afbeeldingen zodat het lijkt dat het spel beweegt.
        window.blit(spel_afbeeldingen['achtergrond'], (0, 0))
        window.blit(spel_afbeeldingen['grond'], (grond, verhoging))
        window.blit(spel_afbeeldingen['flappybird'], (x, y))
        for bovenpijp, onderpijp in zip(boven_pijpen, onder_pijpen):
            window.blit(spel_afbeeldingen['pijp_afbeelding'][0], (bovenpijp['x'], bovenpijp['y']))
            window.blit(spel_afbeeldingen['pijp_afbeelding'][1], (onderpijp['x'], onderpijp['y']))

        nummers = [int(x) for x in list(str(score))]
        breedte = 0
        for num in nummers:
            breedte += spel_afbeeldingen['score_afbeeldingen'][num].get_width()
        xOffset = (window_breedte - breedte) / 1.1

        # Voeg de nummers dan ook toe aan het scherm.
        for num in nummers:
            window.blit(spel_afbeeldingen['score_afbeeldingen'][num], (xOffset, window_breedte * 0.02))

            xOffset += spel_afbeeldingen['score_afbeeldingen'][num].get_width()

        pygame.display.update()
        frames_per_seconden_klok.tick(frames_per_seconden)

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

    spel_afbeeldingen['dood_scherm'] = pygame.image.load(dood_afbeelding).convert_alpha()
    spel_afbeeldingen['start_scherm'] = pygame.image.load(start_afbeelding).convert_alpha()
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
        dood = False

        while True:
            for evenement in pygame.event.get():
                print(evenement.type, QUIT)
                # Een gebruiker kan het spel stoppen door op het kruisje te drukken of op ESC te drukken.
                if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.type == KSCAN_ESCAPE):
                    print('QUIT')
                    pygame.quit()
                    sys.exit()

                # Als de gebruiker op spatie drukt, dan beweegt flappybird.
                elif playButtonPressed:
                    playButtonPressed = False
                    print('PLAY')
                    speel_flappybird()
                    dood = True

                elif rangButtonPressed:
                    rangButtonPressed = False
                    print('RANG')
                    # doe rang

                # Als de gebruiker niets doet dan gebeurt er ook niets.
                else:
                    print('START of DOOD')
                    window.blit(spel_afbeeldingen['achtergrond'], (0, 0))
                    window.blit(spel_afbeeldingen['flappybird'], (x, y))
                    window.blit(spel_afbeeldingen['grond'], (grond, verhoging))
                    if not dood:
                        window.blit(spel_afbeeldingen['start_scherm'], (0, 0))
                        button_start = button.Button(158, 350, start_img, 1)
                        button_rang = button.Button(408, 350, rang_img, 1)
                    else:
                        window.blit(spel_afbeeldingen['dood_scherm'], (0, 0))
                        button_start = button.Button(158, 350, start_img, 1)
                        button_rang = button.Button(408, 350, rang_img, 1)

                    run = True
                    while run:

                        if button_start.draw(window):
                            print("playButtonPressed")
                            playButtonPressed = True
                            run = False

                        if button_rang.draw(window):
                            print("RANG")
                            rangButtonPressed = True
                            run = False

                        for evenement in pygame.event.get():
                            pass

                        pygame.display.update()

                    pygame.display.update()
                    frames_per_seconden_klok.tick(frames_per_seconden)
