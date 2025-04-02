import random

opcje=("kamien","papier","nozyce")
a=random.choice(opcje)
b=input("Podaj swoją opcję: ")
if a==b:
    print("Remis")
elif a=="kamien" and b=="papier":
    print("Wygrałeś")
elif a=="nozyce" and b=="papier":
    print("Przegrałeś")
elif a=="kamien" and b=="nozyce":
    print("Przegrałeś")
elif a=="papier" and b=="nozyce":
    print("Wygrałeś")
elif a=="nozyce" and  b=="kamien":
    print("Wygrałeś")
elif a=="papier" and b=="kamien":
    print("Przegrałeś")
else:
    print("Niepoprawna opcja wpisana")