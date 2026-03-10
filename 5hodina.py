def prvocislocvic():
    cislo = int(input("zadejte cislo: "))
    prvocisla = []
    for j in range(2, cislo + 1):
        prvocislo = True
        for i in range(2, j):
            if j % i == 0:
                prvocislo = False
                break
        if prvocislo:
            prvocisla.append(j)
    print("prvocisla do toho cisla jsou", prvocisla)
 
 
def bankomat():
    vklad = int(input("vlozte prachy: "))
    rozmenit = []
    while (vklad // 5000) > 0:
        rozmenit.append(5000)
        vklad -= 5000
    while (vklad // 2000) > 0:
        rozmenit.append(2000)
        vklad -= 2000
    while (vklad // 1000) > 0:
        rozmenit.append(1000)
        vklad -= 1000
    while (vklad // 500) > 0:
        rozmenit.append(500)
        vklad -= 500 
    while (vklad // 200) > 0:
        rozmenit.append(200)
        vklad -= 200 
    while (vklad // 100) > 0:
        rozmenit.append(100)
        vklad -= 100 
    while (vklad // 50) >0:
        rozmenit.append(50)
        vklad -= 50 
    while (vklad // 20) > 0:
        rozmenit.append(20)
        vklad -= 20 
    while (vklad // 10) > 0:
        rozmenit.append(10)
        vklad -= 10 
    while (vklad // 5) > 0:
        rozmenit.append(5)
        vklad -= 5 
    while (vklad // 2) > 0:
        rozmenit.append(2)
        vklad -= 2 
    while (vklad // 1) > 0:
        rozmenit.append(1)
        vklad -= 1 
    print(rozmenit)
    print(len(rozmenit))

bankomat()