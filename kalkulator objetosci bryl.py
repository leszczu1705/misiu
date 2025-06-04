import math
a=input("Podaj cyfrę, odpowiadającą bryle, której objętość chcesz obliczyć: 1-prostopadłościan, 2-walec, 3-stozek, 4-kula: ")
def prostopadloscian(dlugosc,szerokosc,grubosc):
    if dlugosc >0 and szerokosc>0 and grubosc>0:
        return dlugosc*szerokosc*grubosc
    elif dlugosc<=0 and szerokosc<=0 and grubosc<=0:
        return "Niepoprawna długość, szerokość i grubość prostopadłościanu. Uruchom program jeszcze raz."
    elif dlugosc<=0 and szerokosc<=0:
        return "Niepoprawna długość i szerokość prostopadłościanu. Uruchom program jeszcze raz."
    elif dlugosc<=0 and grubosc<=0:
        return "Niepoprawna długość i grubość prostopadłościanu. Uruchom program jeszcze raz."
    elif szerokosc<=0 and grubosc<=0:
        return "Niepoprawna szerokość i grubość prostopadłościanu. Uruchom program jeszcze raz."
    elif dlugosc<=0:
        return "Niepoprawna długość prostopadłościanu. Uruchom program jeszcze raz."
    elif szerokosc<=0:
        return "Niepoprawna szerokość prostopadłościanu. Uruchom program jeszcze raz."
    else:
        return "Niepoprawna grubość prostopadłościanu. Uruchom program jeszcze raz."
def  walec(promien,wysokosc):
    if promien>0 and wysokosc >0:
        return promien*promien*wysokosc*math.pi
    elif promien<=0 and wysokosc<=0:
        return "Niepoprawna długość promienia i wysokości. Uruchom program jeszcze raz."
    elif promien<=0:
        return "Niepoprawna długość promienia. Uruchom program jeszcze raz."
    else:
        return "Niepoprawna długość wysokości. Uruchom program jeszcze raz."
def stozek(promien,wysokosc):
    if promien>0 and wysokosc>0:
        return promien*promien*wysokosc*math.pi/3
    elif promien<=0 and wysokosc<=0:
        return "Niepoprawna długość promienia i wysokości. Uruchom program jeszcze raz."
    elif promien<=0:
        return "Niepoprawna długość promienia. Uruchom program jeszcze raz."
    else:
        return "Niepoprawna długość wysokości. Uruchom program jeszcze raz."
def kula(promien):
    if promien>0:
        return promien*promien*promien*math.pi*4/3
    else:
        return "Niepoprawna długośc promienia. Uruchom program jeszcze raz."
    


if not a.isdigit():
    print("Zmienna jest tekstem, liczbą niecałkowitą lub liczbą ujemną, a nie liczbą naturalną. Uruchom program ponownie.")
    exit()
a=int(a)
if a==1:
    b=float(input("Podaj długość prostopadłościanu: "))
    c=float(input("Podaj szerokość prostopadłościanu: "))
    d=float(input("Podaj grubość prostopadłościanu: "))
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