#ksuma kwadratów N-liczb pierwszycj
def ciag(n):
    i=1
    suma=0
    while i<=n:
        print(i*i)
        suma=suma+(i*i)
        print(suma)
        i+=1
numer=int(input("podaj numer: "))
ciag(numer)