#wskaźnik bmi o wzorze m/h^2
def wskaznik_bmi(masa, wzrost):
    wzrost=wzrost/100
    bmi=masa/(wzrost*wzrost)
    return bmi
centymetry=float(input("Ile masz w spodniach?"))
kilogramy=float(input("Ile wykręcasz do 100 na wadze?"))
wskaznik=wskaznik_bmi(kilogramy, centymetry)
print(f"Twoje BMI wynosi:  {round(wskaznik, 2)}")

if wskaznik < 18.5:
    print("Niedowaga zacznij coś jeść bo uschniesz")
elif wskaznik >= 18.5 and wskaznik <25:
    print("Waga prawidłowa tak trzymaj")
elif wskaznik >= 25 and wskaznik <30:
    print("Nadwaga, pora się zacząć ruszać grubasku")
else:
    print("O kurwa chłopie, ile ty żresz?!")
