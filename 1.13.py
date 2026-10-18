#program ma pobrać 2 liczby całkowite N takie że N > 2
#oraz K takie że N > K > 0
#wypisuje on liczby od 1 do N pomijając liczby podzielne przez K

def zadanie13(a,b):
    for i in range(1, a):
        if i%b !=0:
            print(i)

x=int(input("Podaj 1 liczbę większą od 2"))
while True:
    if x<2:
        print("Ty umiesz czytać matole?")
        x = int(input("Podaj 1 liczbę większą od 2"))
    else:
        break
y=int(input("Podaj 2 liczbę większą od 0 i mniejszą od N"))
while True:
    if y<0 or y>x:
        print("Ty umiesz czytać matole?")
        y = int(input("Podaj 2 liczbę większą od 0 oraz mniejszą od 1 podanej liczby"))
    else:
        break
zadanie13(x,y)