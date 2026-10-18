#pętla sum licz od 1 do N
def ciag(numer):
    if numer<=0:
        print("no chyba coś cię popierdoliło")
    else:
        i=1
        suma=0
        while i<=numer:
            suma+=i
            print (suma)
            i=i+1
n=int(input("podaj liczbę: "))
ciag(n)