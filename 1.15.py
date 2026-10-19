import random
losowana=random.randint(1,100)
prob=0
while True:
    moja=int(input("Podaj swoją liczbę z działu 1 do 100: "))
    if moja < losowana:
        prob=prob+1
        print("Jest większa")
    elif moja == losowana:
        print(f"Brawo wygrałeś losowana liczba to faktycznie była {losowana}")
        prob = prob + 1
        break
    elif moja > losowana:
        prob = prob + 1
        print("Jest mniejsza od twojej")
print(f"Zajęło ci to {prob} prób")