import pygame
import button
import sys
from pygame.locals import *
import time

window_breedte = 600
window_hoogte = 499
window = pygame.display.set_mode((window_breedte, window_hoogte))
frames_per_seconden = 32
spel_afbeeldingen = {}
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
_key = 'afbeeldingen/_key.png'
wrong = 'afbeeldingen/wrong.png'
spel_afbeeldingen['wrong'] = pygame.image.load(wrong).convert_alpha()
spel_afbeeldingen['*_key'] = pygame.image.load(_key).convert_alpha()
spel_afbeeldingen['achtergrond_key'] = pygame.image.load(achtergrond_key).convert_alpha()


def code_key(computercode):

    global start
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
            print(time.time())
            if (start + 2) < time.time():
                print(time.time())
                wrongCode = False

        else:
            if code == computercode:
                print("De code is juist")
                gevonden = True

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


code_key("3585")
