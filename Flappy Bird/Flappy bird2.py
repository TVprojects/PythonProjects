"""
Dit is Flappy Bird.
Een gebruiker drukt op SPATIE om de vogel te laten vliegen, anders valt de vogel naar beneden.
Als je door een pijp vliegt krijg je punten.
"""

import time
import random
import sys
import pygame as pygame
from pygame.locals import *
import button
import onOff

# Bepaal de hoogte van je speelscherm
window_breedte = 600
window_hoogte = 499

# Configuratie van het spel
autoFly = False
window = pygame.display.set_mode((window_breedte, window_hoogte))
verhoging = window_hoogte * 0.8
spel_afbeeldingen = {}
frames_per_seconden = 32
pijp_afbeelding = 'afbeeldingen/pijp.png'
achtergrond_afbeelding = 'afbeeldingen/achtergrond.jpg'
vogel_afbeelding = 'afbeeldingen/vogel.png'
settings_img = pygame.image.load('afbeeldingen/Settings.png').convert_alpha()
grond_afbeelding = 'afbeeldingen/grond.jfif'
start_afbeelding = 'afbeeldingen/flappy-bird-startscherm.jpg'
dood_afbeelding = 'afbeeldingen/dood_scherm.png'
start_img = pygame.image.load('afbeeldingen/Flappy-start-button.png').convert_alpha()
rang_img = pygame.image.load('afbeeldingen/rang.png').convert_alpha()
back_img = pygame.image.load('afbeeldingen/back.png').convert_alpha()
cheaten_img = pygame.image.load('afbeeldingen/cheaten.png').convert_alpha()
nul_key = pygame.image.load('afbeeldingen/0_key.png').convert_alpha()
een_key = pygame.image.load('afbeeldingen/1_key.png').convert_alpha()
twee_key = pygame.image.load('afbeeldingen/2_key.png').convert_alpha()
drie_key = pygame.image.load('afbeeldingen/3_key.png').convert_alpha()
vier_key = pygame.image.load('afbeeldingen/4_key.png').convert_alpha()
vijf_key = pygame.image.load('afbeeldingen/5_key.png').convert_alpha()
zes_key = pygame.image.load('afbeeldingen/6_key.png').convert_alpha()
zeven_key = pygame.image.load('afbeeldingen/7_key.png').convert_alpha()
acht_key = pygame.image.load('afbeeldingen/8_key.png').convert_alpha()
negen_key = pygame.image.load('afbeeldingen/9_key.png').convert_alpha()
achtergrond_key = 'afbeeldingen/board_key.png'
achtergrond_cheaten = 'afbeeldingen/Cheaten_achtergrond.png'
_key = 'afbeeldingen/_key.png'
wrong = 'afbeeldingen/wrong.png'
spel_afbeeldingen['wrong'] = pygame.image.load(wrong).convert_alpha()
spel_afbeeldingen['*_key'] = pygame.image.load(_key).convert_alpha()
spel_afbeeldingen['achtergrond_key'] = pygame.image.load(achtergrond_key).convert_alpha()
spel_afbeeldingen['achtergrond_cheaten'] = pygame.image.load(achtergrond_cheaten).convert_alpha()
grond = 0
playButtonPressed = False
rangButtonPressed = False
settingsButtonPressed = False
game_code = False


def cheaten():
    global autoFly
    backPressed = False
    button_back = button.Button(500, 2, back_img, 1)
    aanAf = onOff.OnOff(450, 80)
    while not backPressed:
        for evenement in pygame.event.get():
            # Een gebruiker kan het spel stoppen door op het kruisje te drukken of op ESC te drukken.
            if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.key == K_ESCAPE):
                print('QUIT')
                pygame.quit()
                sys.exit()
        window.blit(spel_afbeeldingen['achtergrond_cheaten'], (0, 0))
        backPressed = button_back.draw(window)
        autoFly = aanAf.draw(window, autoFly)
        pygame.display.update()
        frames_per_seconden_klok.tick(frames_per_seconden)


def code_key(computercode):
    global game_code

    if not game_code:
        wrongCode = False
        pogingen = 3
        code = ""
        gevonden = False
        x = 100
        key_ = 0

        window.blit(spel_afbeeldingen['achtergrond_key'], (0, 0))
        button1 = button.Button(219, 191, een_key, 1)
        button2 = button.Button(298, 190, twee_key, 1)
        button3 = button.Button(375, 190, drie_key, 1)
        button4 = button.Button(221, 264, vier_key, 1)
        button5 = button.Button(298, 263, vijf_key, 1)
        button6 = button.Button(376, 262, zes_key, 1)
        button7 = button.Button(222, 338, zeven_key, 1)
        button8 = button.Button(300, 336, acht_key, 1)
        button9 = button.Button(377, 335, negen_key, 1)
        button0 = button.Button(301, 409, nul_key, 1)
        pygame.display.update()

        while not gevonden and pogingen > 0:
            while not len(code) == len(computercode) and not wrongCode:
                for evenement in pygame.event.get():
                    # Een gebruiker kan het spel stoppen door op het kruisje te drukken of op ESC te drukken.

                    if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.key == K_ESCAPE):
                        print('QUIT')
                        pygame.quit()
                        sys.exit()

                    if key_ > 0:
                        pass
                    if evenement.type == MOUSEBUTTONDOWN or evenement.type == MOUSEBUTTONUP:
                        print(evenement.type)
                        if button1.draw(window):
                            code += "1"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button2.draw(window):
                            code += "2"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button3.draw(window):
                            code += "3"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button4.draw(window):
                            code += "4"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button5.draw(window):
                            code += "5"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button6.draw(window):
                            code += "6"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button7.draw(window):
                            code += "7"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button8.draw(window):
                            code += "8"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button9.draw(window):
                            code += "9"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                        if button0.draw(window):
                            code += "0"
                            print(f"Jij gaf dit al in {code}")
                            key_ += 1

                    pygame.display.update()

            if wrongCode:
                window.blit(spel_afbeeldingen['wrong'], (0, 0))
                pygame.display.update()
                if (start + 2) < time.time():
                    wrongCode = False

            else:
                if code == computercode:
                    print("De code is juist")
                    gevonden = True
                    game_code = True
                    cheaten()
                else:
                    pogingen -= 1
                    print(f"Je hebt het fout je hebt nog {pogingen} poging(en) over")
                    wrongCode = True
                    start = time.time()
                    code = ""
                    key_ = 0
                if pogingen == 0:
                    print("Dit gaat er nu gebeuren, om te zien wat er gebeurt klik op de link en bekijk de hele video! "   
                          "https://www.youtube.com/watch?v=GxM3wstBcD4")
    else:
        print('....')
        cheaten()


def settings():
    print('*** SETTINGS ***')
    l_backButtonPressed = False
    cheatenButtonPressed = False
    button_cheaten = button.Button(300, 60, cheaten_img, 1)
    button_back = button.Button(500, 2, back_img, 1)
    while not l_backButtonPressed:
        for evenement in pygame.event.get():
            if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.key == K_ESCAPE):
                print('QUIT')
                pygame.quit()
                sys.exit()
        window.blit(spel_afbeeldingen['settings_afbeeldingen'][0], (0, 0))

        l_backButtonPressed = button_back.draw(window)

        if cheatenButtonPressed:
            cheatenButtonPressed = False
            print('cheaten')
            code_key("1")

        if button_cheaten.draw(window):
            print('cheaten')
            cheatenButtonPressed = True

        pygame.display.update()
        frames_per_seconden_klok.tick(frames_per_seconden)


def genereer_pijp():
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

    # Valt de vogel op de grond?
    if y > verhoging - 25:
        return True

    # Komt de vogel tegen de bovenkant / bovenkant van de pijp?
    for pijp in boven_pijpen:
        xFlappyLinks = x
        xFlappyRechts = x + spel_afbeeldingen['flappybird'].get_width()
        nietRaakX = xFlappyRechts < pijp['x'] or xFlappyLinks > pijp['x'] + pijpbreedte
        welRaakX = not nietRaakX
        if y < pijphoogte + pijp['y'] and welRaakX:
            print("Dood van boven!", x, pijp['x'], pijpbreedte)
            return True
    # Komt de vogel tegen de onderkant / onderkant van de pijp?
    for pijp in onder_pijpen:
        xFlappyLinks = x
        xFlappyRechts = x + spel_afbeeldingen['flappybird'].get_width()
        nietRaakX = xFlappyRechts < pijp['x'] or xFlappyLinks > pijp['x'] + pijpbreedte
        welRaakX = not nietRaakX
        if y + spel_afbeeldingen['flappybird'].get_height() > pijp['y'] and welRaakX:
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
    eerste_pijp = genereer_pijp()
    tweede_pijp = genereer_pijp()

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
                print("QUIT")

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
            if pijp_midden_pos <= speler_midden_pos < pijp_midden_pos + 4: #Dit is voor straks de zelf piloot te laten werken!
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
            nieuwe_pijp = genereer_pijp()
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
    spel_afbeeldingen['settings_afbeeldingen'] = (
        pygame.image.load('afbeeldingen/Settings-achtergrond.png').convert_alpha(),
        pygame.image.load('afbeeldingen/back.png').convert_alpha()
    )

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

    #spel_afbeeldingen['settings_achtergrond'] = pygame.image.load(settings_achtergrond).convert_alpha()
    spel_afbeeldingen['dood_scherm'] = pygame.image.load(dood_afbeelding).convert_alpha()
    spel_afbeeldingen['start_scherm'] = pygame.image.load(start_afbeelding).convert_alpha()
    spel_afbeeldingen['flappybird'] = pygame.image.load(vogel_afbeelding).convert_alpha()
    spel_afbeeldingen['grond'] = pygame.image.load(grond_afbeelding).convert_alpha()
    spel_afbeeldingen['achtergrond'] = pygame.image.load(achtergrond_afbeelding).convert_alpha()
    spel_afbeeldingen['pijp_afbeelding'] = (pygame.transform.rotate(pygame.image.load(pijp_afbeelding).convert_alpha(), 180),
                                                                   pygame.image.load(pijp_afbeelding).convert_alpha())

    print("Welkom bij FlappyBird")
    print("Druk op SPATIE of ENTER om het spel te starten")

    button_start = button.Button(158, 350, start_img, 1)
    button_rang = button.Button(408, 350, rang_img, 1)
    button_settings = button.Button(570, 449, settings_img, 1)

    # Game loop
    while True:

        # Zet bird op de juiste plek
        x = window_breedte // 5
        y = (window_hoogte - spel_afbeeldingen['flappybird'].get_height()) // 2
        dood = False

        while True:
            for evenement in pygame.event.get():
                # Een gebruiker kan het spel stoppen door op het kruisje te drukken of op ESC te drukken.
                if evenement.type == QUIT or (evenement.type == KEYDOWN and evenement.key == K_ESCAPE):
                    print('QUIT')
                    pygame.quit()
                    sys.exit()

            # Als de gebruiker op spatie drukt, dan beweegt flappybird.
            if playButtonPressed:
                playButtonPressed = False
                print('PLAY')
                speel_flappybird()
                dood = True

            elif rangButtonPressed:
                rangButtonPressed = False
                print('RANG')
                # doe rang

            elif settingsButtonPressed:
                settingsButtonPressed = False
                print('SETTINGS')
                settings()
                print('BACK FROM SETTINGS')

            # Als de gebruiker niets doet dan gebeurt er ook niets.
            else:
                window.blit(spel_afbeeldingen['achtergrond'], (0, 0))
                window.blit(spel_afbeeldingen['flappybird'], (x, y))
                window.blit(spel_afbeeldingen['grond'], (grond, verhoging))
                if not dood:
                    window.blit(spel_afbeeldingen['start_scherm'], (0, 0))
                else:
                    window.blit(spel_afbeeldingen['dood_scherm'], (0, 0))

                if button_start.draw(window):
                    print("PlayButtonPressed")
                    playButtonPressed = True
                    run = False

                if button_rang.draw(window):
                    print("RangButtonPressed")
                    rangButtonPressed = True
                    run = False

                if button_settings.draw(window):
                    print("SettingsButtonPressed")
                    settingsButtonPressed = True
                    run = False

                pygame.display.update()
                frames_per_seconden_klok.tick(frames_per_seconden)
