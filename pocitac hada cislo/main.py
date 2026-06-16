import random

def hadani(uhodnute, x, y, vysledky):
    if len(vysledky) > 0:
        print("je cislo vetsi nez? ", max(vysledky))
    else:
        cislo = random.randrange(x, y)
        print(uhodnute)
        if cislo not in uhodnute:
            print("je cislo vetší nez? ", cislo)
        else:
            cislo = random.random(x, y)
            hadani(uhodnute, x, y)
    
    return cislo

def main(x, y, hledane_cislo):
    uhodnute = []
    vysledky = []
    
    while True:
        cislo = hadani(uhodnute, x, y, vysledky)

        uhodnute.append(cislo)
        user = input("a/n: ")
        if user == "a":
            for i in range(cislo):
                vysledky.append(i)

        print(vysledky)


print("zadejte (1) pro 1-10")
print("zadejte (2) pro 1-50")
print("zadejte (3) pro 1-100")
print("zadejte (4) pro vlastni rozsah")
print("zadejte (5) pro konec")

while True:
    user_input = int(input(" "))

    if user_input:
        hledane_cislo = int(input("zadejte cislo ktere chcete aby pocitac hadal: "))
        
    if user_input == 1:
        main(0, 10, hledane_cislo)
    if user_input == 2:
        main(0, 50, hledane_cislo)
    if user_input == 3:
        main(0, 100, hledane_cislo)
    if user_input == 4:
        pass
    if user_input == 5:
        break


    