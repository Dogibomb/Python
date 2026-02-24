def cykly():
    for i in range(50,101, 5):
        print(i)
    
    print()

    i = 50
    while(i < 101):
        print(i)
        i += 5

    print()

    for i in range(100, 50, -5):
        print(i)
    
    print()

    i = 100
    while(i >= 50):
        print(i)
        i -= 5

def cykl2():
    zacatek = int(input("zadejte cislo od: "))
    konec = int(input("zadejte cislo do: "))
    krok = int(input("zadej krok: "))

    if zacatek < konec:
        for i in range(zacatek, konec+1, krok):
            print(i)
    else:
        for i in range(zacatek, konec-1, krok*(-1)):
            print(i)

def cykl3():
    zacatek = int(input("zadejte cislo od: "))
    konec = int(input("zadejte cislo do: "))
    krok = int(input("zadej krok: "))

    cisla = []

    for i in range(zacatek, konec+1, krok):
        cisla.append(i)
    
    print(cisla)
    print("cisel je: ", len(cisla))
    print("prumer", sum(cisla)/len(cisla))
    

def cykl4():
    cisla = []
    while(True):
        a = int(input("zadejte cislo: "))
        if a == 0:
            break
        cisla.append(a)
    
    cisla.sort()
    print(cisla)
    print("suma cisel je: ", sum(cisla))
    print("cisel je:  ", len(cisla))
    print("prumer cisel je: ", sum(cisla)/len(cisla))
    print("nejvetsi cislo je: ", cisla[len(cisla)-1])

cykl4()