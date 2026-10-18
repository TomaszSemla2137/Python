def sila_wiatru(wiatr):
    if wiatr <0:
        print("Co tam się kurwa dzieje? Zasysa was?")
        wiatr=wiatr*-1
    if wiatr <1:
        print("Cisza")
    elif wiatr <=3:
        print("zefir")
    elif wiatr <=27:
        print("bryza")
    elif wiatr <=47:
        print("wichura")
    elif wiatr <=63:
        print("sztorm")
    else :
        print("Huragan Beata")

jak_wieje= float(input("Podaj siłę wiatru: "))
sila_wiatru(jak_wieje)