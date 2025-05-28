a=int(input("Podaj pierwszą liczbę naturalną: "))
b=int(input("Podaj drugą liczbę naturalną: "))
if a>0 and b>0:
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    print(a)
elif a<=0 and b<=0:
    print("Obie liczby nie są większe od zera. Podaj liczby ponownie")
elif a<=0:
    print("Pierwsza liczba jest mniejsza od zera. Podaj liczby ponownie")
else:
    print("Druga liczba jest mniejsza od zera. Podaj liczby ponownie")