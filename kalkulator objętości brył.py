import math
a=int(input("Podaj liczbę 1-prostopadłościan, 2-walec, 3-stozek, 4-kula: "))
def prostopadloscian(bok1,bok2,bok3):
    if bok1 >0 and bok2>0 and bok3>0:
        return bok1*bok2*bok3
    else: 
        return "Zła długość boku"
def  walec(promień,wysokość):
    if promień>0 and wysokość >0:
        return promień*promień*wysokość*math.pi
    else:
        return "Zła liczba"
def stozek(promień,wysokość):
    if promień>0 and wysokość>0:
        return promień*promień*wysokość*math.pi/3
    else:
        return "Zła liczba"
def kula(promień):
    if promień>0:
        return promień*promień*promień*math.pi*4/3
    else:
        return "Zła liczba"
if a==1:
    b=float(input("Podaj długość pierwszego boku: "))
    c=float(input("Podaj długość drugiego boku: "))
    d=float(input("Podaj długość trzeciego boku: "))
    print(prostopadloscian(b,c,d))
elif a==2:
    b=float(input("Podaj długość promienia podstawy: "))
    c=float(input("Podaj długość wysokości walca: "))
    print(walec(b,c))
elif a==3:
    b=float(input("Podaj długość promienia podstawy: "))
    c=float(input("Podaj długość wysokości stozka"))
    print(stozek(b,c))
elif a==4:
    b=float(input("Podaj długość promienia kuli: "))
    print(kula(b))
else:
    print("Taka cyfra nie odpowiada zadnej bryle. Podaj cyfrę ponownie.")