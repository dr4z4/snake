# Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) 
# a vypíše je jako mapu: mřížku 10×10, kde na políčka, která jsou v seznamu, napíše X, jinde tečku. Například:

# nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])
# X X . . . . . . . .
# . . . . . . . . . .
# . . X . . . . . . .
# . . . . X . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . X .

# Jak na to?
#     Udělej tabulku (seznam seznamů) se samými tečkami, něco jako:
#     [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']].
#     Na příslušných místech nahraď tečky X-ky.
#     Tabulku vypiš pomocí dvou cyklů for zanořených do sebe.


def nakresli_mapu(seznam_souradnic):
    """Funkce dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) 
    a vypíše je jako mapu: mřížku 10×10, kde na políčka, která jsou v seznamu, napíše X, jinde tečku."""

    mapa_tecek = list(list('.' * 10) for i in range(10))

    for x, y in seznam_souradnic:
        mapa_tecek[y][x] = 'X'
    for y in range(1):   #celý "řádek"...y
        for x in range(len(mapa_tecek)):
            # print(mapa_tecek[x])
            print(' '.join(mapa_tecek[x]))

nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

# Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a
#  přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:
# souradnice = [(0, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
# Funkce by neměla nic vracet. Jen mění už existující seznam.



def pohyb(seznam_souradnic, svet_strana):
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
    print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]"""

    smery_pohybu = {
    's': (0, -1),
    'j': (0, 1),
    'v': (1, 0),
    'z': (-1, 0)}
    
    if not seznam_souradnic:   # ošetření, pokud by někdo poslal prázdný seznam souřadnic
        seznam_souradnic.append((0, 0))
        vektor = smery_pohybu[svet_strana]              # např. (0, -1)
        posledni_souradnice = seznam_souradnic[-1]      # např. (2, 2)
        nova_souradnice = (posledni_souradnice[0] + vektor[0], posledni_souradnice[1] + vektor[1])  # součet - např. (2, 1)
        seznam_souradnic.append(nova_souradnice)
    elif seznam_souradnic:
        vektor = smery_pohybu[svet_strana]              # např. (0, -1)
        posledni_souradnice = seznam_souradnic[-1]      # např. (2, 2)
        nova_souradnice = (posledni_souradnice[0] + vektor[0], posledni_souradnice[1] + vektor[1])  # součet - např. (2, 1)
        seznam_souradnic.append(nova_souradnice)

# souradnice = [(0, 0), (0, 1)]
# pohyb(souradnice, 'v')
# print(souradnice)         
# pohyb(souradnice, 'v')
# print(souradnice)         
# pohyb(souradnice, 'j')
# print(souradnice)        
# pohyb(souradnice, 's')
# print(souradnice)         

# souradnice = [(0, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]"""

# souradnice = []
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]"""

# # Napiš cyklus, který se bude ptát uživatele na světovou stranu, podle ní zavolá pohyb, 
# # a následně vykreslí seznam jako mapu. Pak se opět se zeptá na stranu atd.
# # Začínej se seznamem [(0, 0), (1, 0), (2, 0)].
seznam_souradnic = [(0, 0), (1, 0), (2, 0)]
while True:
    smer = input('Zadej směr pohybu - "s" pro sever, "v" pro východ, "j" pro jih, "z" pro západ: ')
    pohyb(seznam_souradnic, smer)
    nakresli_mapu(seznam_souradnic)

