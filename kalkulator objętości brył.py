import math
a=int(input("Podaj liczbę 1-prostopadłościan, 2-walec, 3-stozek, 4-kula: "))
def prostopadloscian(bok1,bok2,bok3):
    if bok1 >0 and bok2>0 and bok3>0:
        return bok1*bok2*bok3
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
def  walec(promień,wysokość):
    if promień>0 and wysokość >0:
        return promień*promień*wysokość*math.pi
    elif promień<=0 and wysokość<=0:
        return "Niepoprawna długość promienia i wysokości"
    elif promień<=0:
        return "Niepoprawna długość promienia"
    else:
        return "Niepoprawna długość wysokości"
def stozek(promień,wysokość):
    if promień>0 and wysokość>0:
        return promień*promień*wysokość*math.pi/3
    elif promień<=0 and wysokość<=0:
        return "Niepoprawna długość promienia i wysokości"
    elif promień<=0:
        return "Niepoprawna długość promienia"
    else:
        return "Niepoprawna długość wysokości"
def kula(promień):
    if promień>0:
        return promień*promień*promień*math.pi*4/3
    else:
        return "Niepoprawna długośc promienia"
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