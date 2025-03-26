import math
a=int(input("Podaj liczbę 1-prostopadłościan, 2-walec, 3-ostrosłup, 4-stozek, 5-kula: "))
def prostopadloscian(bok1,bok2,bok3):
    if bok1 >0 and bok2>0 and bok3>0:
        return bok1*bok2*bok3
    else: 
        return "Zła liczba"
def  walec(promień,wysokość):
    if promień>0 and wysokość >0:
        return promień*wysokość*math.pi
    else:
        return "Zła liczba"
def ostroslup(bok1,bok2,wysokość):
    if bok1>0 and wysokość>0 and bok2>0:
        return bok1*bok2*wysokość/3
    else:
        return "Zła liczba"
def stozek(promień,wysokość):
    if promień>0 and wysokość>0:
        return promień*wysokość*math.pi/3
    else:
        return "Zła liczba"
def kula ():