import random


def Hoger_Lager():
    getal = 50
    fout = 0
    reeks = 10000

    while fout == 0:

        hoger_lager = input(f"Denk je dat het volgende getal h/l is dan {getal}? ")
        getal2 = random.randint(0, 100)

        if hoger_lager == "h" and getal < getal2:
            print("Je hebt het juist")
            reeks += 1
        elif hoger_lager == "l" and getal > getal2:
            print("Je hebt het juist")
            reeks += 1
        else:
            print(f"Je hebt het fout het getal was {getal2}")
            fout = 1
            break
        print(f"Jij zij {hoger_lager} dan {getal}.")
        getal = getal2
    print(f"Je reeks is {reeks}")


Hoger_Lager()



