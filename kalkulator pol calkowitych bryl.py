import math
a=int(input("Podaj liczbę, odpowiadającą bryle ,której pole powierzchni calkowitej chcesz obliczyć: 1-prostopadłościan, 2-walec, 3-stozek, 4-kula: "))
def prostopadloscian(bok1,bok2,bok3):
    if bok1>0 and bok2>0 and bok3>0:
        return 2*(bok1*bok2+bok2*bok3+bok1*bok3)
    elif bok1<=0 and bok2<=0 and bok3<=0:
        return "Niepoprawna długość wszystkich trzech boków. Uruchom program jeszcze raz."
    elif bok1<=0 and bok2<=0:
        return "Niepoprawna długość pierwszego i drugiego boku. Uruchom program jeszcze raz."
    elif bok1<=0 and bok3<=0:
        return "Niepoprawna długość pierwszego i trzeciego boku. Uruchom program jeszcze raz."
    elif bok2<=0 and bok3<=0:
        return "Niepoprawna długość drugiego i trzeciego boku. Uruchom program jeszcze raz."
    elif bok1<=0:
        return "Niepoprawna długośc pierwszego boku. Uruchom program jeszcze raz."
    elif bok2<=0:
        return "Niepoprawna długość drugiego boku. Uruchom program jeszcze raz."
    else:
        return "Niepoprawna długość trzeciego boku. Uruchom program jeszcze raz."
def walec(promien,wysokosc):
    if promien>0 and wysokosc>0:
        return 2*math.pi*promien*(promien+wysokosc)
    elif promien<=0 and wysokosc<=0:
        return "Niepoprawna długość promienia i wysokości. Uruchom program jeszcze raz."
    elif promien<=0:
        return "Niepoprawna długość promienia. Uruchom program jeszcze raz."
    else:
        return "Niepoprawna długość wysokości. Uruchom program jeszcze raz."
def stozek(promien,tworzaca):
    if promien>0 and tworzaca>0:
        return math.pi*promien*(promien+tworzaca)
    elif promien<=0 and tworzaca<=0:
        return "Niepoprawna długość promienia i tworzącej. Uruchom program jeszcze raz."
    elif promien<=0:
        return "Niepoprawna długość promienia. Uruchom program jeszcze raz."
    else:
        return "Niepoprawna długość tworzącej. Uruchom program jeszcze raz."
def kula(promien):
    if promien>0:
        return 4*math.pi*promien*promien
    else:
        return "Niepoprawna długość promienia. Uruchom program jeszcze raz."
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
    c=float(input("Podaj długość tworzącej stozka: "))
    print(stozek(b,c))
elif a==4:
    b=float(input("Podaj długość promienia kuli: "))
    print(kula(b))
else:
    print("Taka cyfra nie odpowiada zadnej bryle. Wprowadź cyfrę jeszcze raz.")