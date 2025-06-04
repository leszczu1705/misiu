import math
a=input("Podaj litery, odpowiadającą bryle, której pole powierzchni calkowitej chcesz obliczyć: 1-prostopadłościan, 2-walec, 3-stozek, 4-kula: ")
if not a.isdigit():
    print("Zmienna jest tekstem, liczbą niecałkowitą lub liczbą ujemną, a nie liczbą naturalną. Uruchom program ponownie.")
    exit()
a=int(a)
def prostopadloscian(dlugosc,szerokosc,grubosc):
    if dlugosc >0 and szerokosc>0 and grubosc>0:
        return 2*(dlugosc*szerokosc+szerokosc*grubosc+dlugosc*grubosc)
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
    c=float(input("Podaj długość tworzącej stozka: "))
    print(stozek(b,c))
elif a==4:
    b=float(input("Podaj długość promienia kuli: "))
    print(kula(b))
else:
    print("Taka cyfra nie odpowiada zadnej bryle. Wprowadź cyfrę jeszcze raz.") 