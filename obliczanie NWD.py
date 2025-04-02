a=int(input("Podaj pierwszą liczbę całkowitą większą od zera: "))
b=int(input("Podaj drugą liczbę całkowitą większą od zera: "))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)