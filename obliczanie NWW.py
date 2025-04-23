a=int(input("Podaj pierwszą liczbę całkowitą większą od zera: "))
b=int(input("Podaj drugą liczbę całkowitą większą od zera: "))
c=a
d=b
if a>0 and b>0:
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    e=c*d/a
    print(e)
elif a<=0 and b<=0:
    print("Obie liczby nie są większe od zera. Podaj liczby ponownie")
elif a<=0:
    print("Pierwsza liczba jest mniejsza od zera. Podaj liczby ponownie")
else:
    print("Druga liczba jest mniejsza od zera. Podaj liczby ponownie")