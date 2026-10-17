#liczenie roku przestępnego
#warunki:
#jest podzielny przez 400
#jest podzielny przez 100
#jest pozielny przez 4
def przestepny(rok):
    if rok&400==0 or rok%100==0 or rok%4==0:
        print("Rok jest przestępny")
    else:
        print("Rok nie jest przestępny")
rok=int(input("Podaj rok: "))
przestepny(rok)