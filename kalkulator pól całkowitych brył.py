import math
a=int(input("Podaj liczbę 1-prostopadłościan, 2-walec, 3-stozek, 4-kula: "))
def prostopadloscian(bok1,bok2,bok3):
    if bok1>0 and bok2>0 and bok3>0:
        return 2(bok1*bok2+bok2*bok3+bok1*bok3)
    elif bok1<=0 and bok2<=0 and bok3<=0:
        return "Niepoprawna długość wszystkich trzech boków"
    elif bok1<=0 and bok2<=0:
        return "Niepoprawna długość pierwszego i drugiego boku"
    elif bok1<=0 and bok3<=0:
        return "Niepoprawna długość pierwszego i trzeciego boku"
    elif bok2<=0 and bok3<=0:
        return "Niepoprawna długość drugiego i trzeciego boku"
    elif bok1<=0:
        return "Niepoprawna długośc pierwszego boku"
    elif bok2<=0:
        return "Niepoprawna długość drugiego boku"
    else:
        return "Niepoprawna długość trzeciego boku"