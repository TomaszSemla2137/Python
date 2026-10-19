#sprawdza czy podana iczba jest pierwsza jeśli nie jest pierwsza przerywa
#gdy jest pierwsza leci dalej
def czy_pierwsza(n):
    if n<=1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
x=int(input("Dawaj liczby pierwsze gałganie: "))
while czy_pierwsza(x):
    print("Masz rację lecisz dalej")
    x = int(input(" "))
print("Ta liczba nie jest pierwsza, no i kasujemy windowsa")