"""""
spelregels
23 spel is over
63 spel is gewonnnen
25 en 45 is terug naar start
10, 20, 30, 40, 50, 60, houd in dat je het geworpen aantal nog een keer loopt
"""

import random
from functies import doe_gooi

print("Welkom bij ganzebord!\nDruk op q als je wil stoppen!")

plaats = 0

while True:
    gooi = input("Gooi je dobbelsteen (g)\n")
    if gooi == 'q':
        break
    elif gooi == 'g':
        worp = random.randint(1, 6)
        print(f"Je worp is {worp}")
        plaats = doe_gooi(plaats, worp)
        if plaats == -1:
            break
    else:
        print("Je mag alleen q en g gebruiken!")
