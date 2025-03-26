import math

a=int(input("Podaj liczbę: 1-trójkąt, 2-prostokąt, 3-trapez, 4-koło, 5-romb, 6-równoległobok"))
def trojkat(bok, wysokość):
    if bok>0 and wysokość>0:
        return bok*wysokość/2
    else:
        return "Zła liczba"
def prostokat(bok1,bok2):
    if bok1>0 and bok2>0:
        return bok1*bok2
    else:
        return "Zła liczba"
def trapez(podstawa1,podstawa2,wysokość):
    if podstawa1>0 and podstawa2 >0 and wysokość>0:
        return (podstawa1+podstawa2)*wysokość/2
    else:
        return "Zła liczba"
def kolo(promień):
    if promień>0:
        return promień*math.pi
    else:
        return "Zła liczba"
def rownoleglobok(podstawa,wysokość):
    if podstawa>0 and wysokość>0:
        return podstawa*wysokość
    else:
        return "Zła liczba"
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
    liczba=int
    b=float(input("Podaj długość boku: "))
    c=float(input("Podaj długość wysokośc iopadającej na ten bok: "))
    print(rownoleglobok(b,c))
else:
    print("Takiej figury nie obsługujemy")