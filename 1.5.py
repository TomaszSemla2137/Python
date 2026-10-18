def oceny(wynik):
    if wynik<0:
        print("Aż tak głupi nie możesz być")
        wynik=wynik*-1
    if wynik <60:
        print("E")
    elif wynik <70:
        print("D")
    elif wynik <80:
        print("C")
    elif wynik <90:
        print("B")
    elif wynik <=100:
        print("A")
    else:
        print("O CHŁOPIE WYJEBAŁO CIĘ POZA SKALE!")

wynik=int(input("Podaj swój wnik procenotwy gałganie"))
oceny(wynik)