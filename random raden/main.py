import random

aantalkeer = 1
min = 1
max = 100

record_bestand = open("record", "r")
wereldrecord = int(record_bestand.read(10))
record_bestand.close()

print("Raad een getal tussen ", min, " en ", max, "raad jij het sneller dan in", wereldrecord, "pogingen?")
raad_mij = random.randint(min, max)



def vraag():
    return int(input("Wat denk je dat het getal is? "))

gebruiker_raad = vraag()

while raad_mij != gebruiker_raad:
    aantalkeer += 1
    if gebruiker_raad > raad_mij:
        print("Je zit te hoog! ")
        gebruiker_raad = vraag()
    elif gebruiker_raad < raad_mij:
        print("Je zit te laag! ")
        gebruiker_raad = vraag()

print("Je hebt het geraden in ", aantalkeer, " keer! ")

if wereldrecord > aantalkeer:
    record_bestand = open("record", "w")
    record_bestand.write(str(aantalkeer))
    print("Je hebt het record verbroken!")
    record_bestand.close()
else:
    print("Je hebt het record niet verbroken ☹ probeer nog eens!")
