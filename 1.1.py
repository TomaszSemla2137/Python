kwota = float(input("Podaj całkowity koszt swoich zakupów:"))
if 0 < kwota <= 100:
    kwota=kwota-(0.1*kwota)
elif kwota > 100:
    kwota=kwota-(0.2*kwota)

print("Kwota twoich zakupów to: ", kwota)