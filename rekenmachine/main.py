while True:
    try:
        Getal1 = float(input("Voer je eerste getal in: "))
        Bewerking = input("Voer je bewerking in ")
        Getal2 = float(input("Voer je tweede getal in: "))

        if Bewerking == "+":
           print(Getal1 + Getal2)
        elif Bewerking == "-":
             print(Getal1 - Getal2)
        elif Bewerking == "*":
             print(Getal1 * Getal2)
        elif Bewerking == "/":
             print(Getal1 / Getal2)
    except:
        print("Je hebt iets fout gedaan!")