# Vylepšení z lekce 9 
from random import randrange

def nakresli_mapu(seznam_souradnic, ovoce):
    """Funkce dostane seznam souřadnic hada (párů čísel menších než 10, která určují sloupec a řádek) 
    a vypíše je jako mapu: mřížku 10×10, kde na políčka, která jsou v seznamu, napíše X, jinde tečku.
    Dále dostane seznam souřadnic ovoce - na tato místa napíše ?."""

    mapa_tecek = list(list('.' * 10) for i in range(10))

    for x, y in seznam_souradnic:
        mapa_tecek[y][x] = 'X'
    for x, y in ovoce:
        mapa_tecek[y][x] = '?'
    for y in range(1):   #celý "řádek"...y
        for x in range(len(mapa_tecek)):
            print(' '.join(mapa_tecek[x]))


# Doplň funkci pohyb tak, aby při pohybu umazala první bod ze seznamu souřadnic.
#  Výsledný seznam tak bude mít stejnou délku, jako před voláním.

# Doplň funkci pohyb tak, aby zamezila:
#     pohybu ven z mapy,
#     pohybu na políčko, které už v seznamu je.
# Vhodná výjimka pro tyto situace je ValueError('Game over').

def pohyb(seznam_souradnic, svet_strana, ovoce):
    """Funkce dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a
    přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:
    souradnice = [(0, 0)]
    pohyb(souradnice, 'v')
    print(souradnice)         # → [(0, 0), (1, 0)]
    pohyb(souradnice, 'v')
    print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
    pohyb(souradnice, 'j')
    print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
    pohyb(souradnice, 's')
    print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
    ¨Dalším argumentem je ovoce - potrava pro hada"""

    smery_pohybu = {
    's': (0, -1),
    'j': (0, 1),
    'v': (1, 0),
    'z': (-1, 0)}
    
    if not seznam_souradnic:   # ošetření, pokud by někdo poslal prázdný seznam souřadnic
        seznam_souradnic.append((0, 0))
    # else: # Nadbytečné!
    #     vektor = smery_pohybu[svet_strana]              # např. (0, -1)
    #     posledni_souradnice = seznam_souradnic[-1]      # např. (2, 2)
    #     nova_souradnice = (posledni_souradnice[0] + vektor[0], posledni_souradnice[1] + vektor[1])  # součet - např. (2, 1)
    #     seznam_souradnic.append(nova_souradnice)
    #     seznam_souradnic.pop(0)
    vektor = smery_pohybu[svet_strana]              # např. (0, -1)
    posledni_souradnice = seznam_souradnic[-1]      # např. (2, 2)
    nova_souradnice = (posledni_souradnice[0] + vektor[0], posledni_souradnice[1] + vektor[1])  # součet - např. (2, 1)
    if (                                                    #JV k nova_souradnice: jen kosmeticky: ty kulate zavorky nepotrebujes, jsou nepovinne.
            nova_souradnice in seznam_souradnic or
            not ( 0 <= nova_souradnice[0] <= 9 ) or
            not ( 0 <= nova_souradnice[1] <= 9 ) 
# nova_souradnice[0] < 0 or nova_souradnice[0] >= 10 
# muzes zapsat jako:
# not ( 0 <= nova_souradnice[0] <= 9 )
    ):
        raise ValueError('Game over!')  #ukončuje běh fce

    seznam_souradnic.append(nova_souradnice)
    if nova_souradnice in ovoce:
        ovoce.remove(nova_souradnice)
        if not ovoce:
            pridej_ovoce(seznam_souradnic, ovoce)
    else:
        seznam_souradnic.pop(0)

def pridej_ovoce(seznam_souradnic, ovoce):
    """Argument - seznam souřadnic hada, již existující ovoce. Funkce vygeneruje 'ovoce', 
    jehož souřadnice není v seznamu souř. hada."""
    while True:
        nahodna_souradnice = (randrange(0,10), randrange(0,10))
        if nahodna_souradnice not in seznam_souradnic:
            ovoce.append(nahodna_souradnice)
            return ovoce

def hra():
    seznam_souradnic = [(0, 0), (1, 0), (2, 0)] #seznam souřadnic hada
    ovoce = [(2, 3)] 
    nakresli_mapu(seznam_souradnic, ovoce)
    pohyby = 0
    while len(seznam_souradnic) < 100:
        smer = input('Zadej směr pohybu - "s" pro sever, "v" pro východ, "j" pro jih, "z" pro západ: ')
        if smer not in "szjv":   # nebo if smer not in ["s", "j", "v", "z"]: nebo if smer != "s" and smer != "v" and smer != "j" and smer != "z":
            print("Špatně zadaný směr pohybu!")
        else:
            pohyb(seznam_souradnic, smer, ovoce)
            pohyby += 1
            if pohyby % 30 == 0:
                pridej_ovoce(seznam_souradnic, ovoce)
            nakresli_mapu(seznam_souradnic,ovoce)
    print("Vyhrál(a) jsi!")

hra()

# Přidej do hry hadí potravu. Tady jsou pravidla pro vegetariánského hada, ale můžeš si je změnit podle chuti:
# Seznam ovoce obsahuje na začátku jedno ovoce na políčku, na kterém není had (například: [(2, 3)] 
# znamená jedno ovoce na pozici (2, 3)).
# Když had sežere ovoce, vyroste („nesmaže“ se mu ocas, tedy neprovede se to, cos přidala v projektu 3), 
# a pokud na mapě zrovna není další ovoce, na náhodném místě (kde není had) vyroste ovoce nové.
# Každých 30 tahů vyroste nové ovoce samo od sebe.
# Na mapě se toto tajemné ovoce zobrazuje jako otazník (?).