a=input("Podaj pierwszą liczbę naturalną: ")
b=input("Podaj drugą liczbę naturalną: ")
if not a.isdigit() and not b.isdigit():
    print("Obie zmienne są liczbami niecałkowitymi lub tekstami, lub liczbami mniejszymi od zera. Uruchom program ponownie.")
    exit()
if not a.isdigit():
    print("Pierwsza zmienna jest liczbą niecałkowitą lub tekstem, lub liczbą mniejszą od zera. Uruchom program ponownie.")
    exit()
if not b.isdigit():
    print("Druga zmienna jest liczbą niecałkowitą lub tekstem, lub liczbą mniejszą od zera. Uruchom program ponownie.")
    exit()
a=int(a)
b=int(b)
c=a
d=b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
e=c*d/a
print(e)