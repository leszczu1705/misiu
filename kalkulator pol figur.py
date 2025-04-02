import math

a=int(input("Podaj liczbę: 1-trójkąt, 2-prostokąt, 3-trapez, 4-koło, 5-romb, 6-równoległobok, 7-deltoid, 8-sześciokąt foremny: "))
def trojkat(bok, wysokość):
    if bok>0 and wysokość>0:
        return bok*wysokość/2
    elif bok<=0 and wysokość<=0:
        return "Niepoprawna długość boku i wysokości"
    elif bok<=0:
        return "Niepoprawna długość boku"
    else:
        return "Niepoprawna długość wysokości"
def prostokat(bok1,bok2):
    if bok1>0 and bok2>0:
        return bok1*bok2
    elif bok1<=0 and bok2<=0:
        return "Niepoprawna długość obu boków"
    elif bok1<=0:
        return  "Niepoprawna długość pierwszego boku"
    else:
        return "Niepoprwawna długość drugiego boku"
def trapez(podstawa1,podstawa2,wysokość):
    if podstawa1>0 and podstawa2 >0 and wysokość>0:
        return (podstawa1+podstawa2)*wysokość/2
    elif podstawa1<=0 and podstawa2<=0 and wysokość<=0:
        return "Niepoprawna długość obu podstaw i wysokości"
    elif podstawa1<=0 and podstawa2<=0:
        return "Niepoprawna długość obu podstaw"
    elif podstawa1<=0 and wysokość<=0:
        return "Niepoprawna długość pierwszej podstawy i wysokości"
    elif podstawa2<=0 and wysokość<=0:
        return "Niepoprawna długość drugiej podstawy i wysokości"
    elif podstawa1<=0:
        return "Niepoprawna długośc pierwszej podstawy"
    elif podstawa2<=0:
        return "Niepoprawna długość drugiej podstawy"
    else:
        return "Niepoprawna długość wysokości"
def kolo(promień):
    if promień>0:
        return promień*math.pi
    else:
        return "Niepoprawna długość promienia koła"
def rownoleglobok(podstawa,wysokość):
    if podstawa>0 and wysokość>0:
        return podstawa*wysokość
    elif podstawa<=0 and wysokość<=0:
        return "Niepoprawna długość podstawy i wysokości"
    elif podstawa<=0:
        return "Niepoprawna długość podstawy"
    else:
        return "Niepoprawna długość wysokości"
def romb(przekątna1, przekątna2):
    if przekątna1>0 and przekątna2>0:
        return 1/2*przekątna1*przekątna2
    elif przekątna1<=0 and przekątna2<=0:
        return "Niepoprawna długość obu przekątnych"
    elif przekątna1<=0:
        return "Niepoprawna długość pierwszej przekątnej"
    else:
        return "Niepoprawna długośąć drugiej przekątnej"
def szesciokat(bok):
    if bok>0:
        return 1.5*bok*bok*math.sqrt(3)
    else:
        return "Niepoprawna długość boku sześciokąta"
if a==1:
    b=float(input("Podaj długość boku: "))
    c=float(input("Podaj długość wysokości opadającej na ten bok: "))
    print(trojkat(b,c))
elif a==2:
    b=float(input("Podaj długość pierwszego boku: "))
    c=float(input("Podaj długośc drugiego boku: "))
    print(prostokat(b,c))
elif a==3:
    b=float(input("Podaj długość pierwszej podstawy: "))
    c=float(input("Podaj długośc drugiej podstawy: "))
    d=float(input("Podaj długość wysokości trapezu: "))
    print(trapez(b,c,d))
elif a==4:
    b=float(input("Podaj długość promienia koła: "))
    print(kolo(b))
elif a==5:
    liczba=int(input("Podaj sposób w jaki sposób chcesz obliczyć pole rombu: 1-0,5*przękątna1*przekątna2  2-podstawa*wysokość: "))
    if liczba==2:
        b=float(input("Podaj długość boku: "))
        c=float(input("Podaj długość wysokości opadającej na ten bok: "))
        print(rownoleglobok(b,c))
    else:
        b=float(input("Podaj długość pierwszej przekątnej: "))
        c=float(input("Podaj długość drugiej przekątnej: "))
        print(romb(b,c))
elif a==6:
        b=float(input("Podaj długość boku: "))
        c=float(input("Podaj długość wysokośc iopadającej na ten bok: "))
        print(rownoleglobok(b,c))
elif a==7:
        b=float(input("Podaj długość pierwszej przekątnej: "))
        c=float(input("Podaj długość drugiej przekątnej: "))
        print(romb(b,c))
elif a==8:
    b=float(input("Podaj długość boku: "))
    print(szesciokat(b))
else:
    print("Taka cyfra nie odpowiada zadnej figurze. Podaj cyfrę ponownie.")