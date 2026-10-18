def przelicznik (sekundy):
    start=sekundy
    minuty=sekundy//60
    sekundy=sekundy%60
    godziny = minuty //60
    minuty = minuty % 60
    doby=godziny //24
    godziny=godziny%24
    miesiace=doby//30
    doby=doby%30
    lata=miesiace//12
    miesiace=miesiace%12
    print(f"{start} sekund to: {lata} lat {miesiace} miesięcy {doby} dni {godziny} godzin {minuty} minut {sekundy} sekund ")
sekund=int(input("podaj liczbę sekund"))
przelicznik(sekund)