bonus_plaatsen = [10, 20, 30, 40, 50, 60]

ja_nee_voor_test = ""


def zet_ja_nee(p_waarde):
    global ja_nee_voor_test
    ja_nee_voor_test = p_waarde


def vraag_ja_nee(p_vraag):
    global ja_nee_voor_test
    if ja_nee_voor_test == "ja":
        ja_nee_voor_test = ""
        return "ja"
    elif ja_nee_voor_test == "nee":
        ja_nee_voor_test = ""
        return "nee"
    else:
        return input(p_vraag)


def doe_gooi(p_plaats, p_worp):
    p_plaats += p_worp
    print(f"Je staat op plaats {p_plaats}")
    l_check = bonus_plaatsen.count(p_plaats)
    if l_check > 0:
        p_plaats += p_worp
        print(f"Je hebt bonus dus het dubbele aantal stapjes! Je staat op plaats {p_plaats}")

    if p_plaats == 25 or p_plaats == 45:
        p_plaats = 0
        print(f"Je hebt ongeluk je moet terug naar start we beginnen opnieuw, je plaats is {p_plaats}")

    elif p_plaats == 63:
        opniew_spelen = vraag_ja_nee("Je hebt gewonnen! Het spel is uit gespeelt wil je nog eens? (ja/nee)")
        if opniew_spelen == 'ja':
            p_plaats = 0

    if p_plaats > 63:
        over_eindstreep = p_plaats
        over_eindstreep -= 63
        p_plaats = 63 - over_eindstreep

    if p_plaats == 23:
        gevangenis = input("Je zit in de gevangenis wil je terug op nieuw beginnen? (ja/nee)")
        if gevangenis == 'ja':
            p_plaats = 0
            print(f"We beginnen opnieuw, je plaats is {p_plaats}")
        elif gevangenis == 'nee':
            p_plaats = -1
        else:
            print("Je mag alleen ja of nee antwoorden!")
    return p_plaats
