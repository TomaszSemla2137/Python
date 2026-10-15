plec=input("Podaj plec: ")
if plec=="K":
    wiek= int(input("Ile masz lat dziewczynko?"))
    if 10<= wiek <= 12:
        print("Witamy w drużynie młoda damo")
    else:
        print("niestety nie mamy miejsca dla osób w twoim wieku")
else:
    print("Wypierdalaj ty zboczeńcu")