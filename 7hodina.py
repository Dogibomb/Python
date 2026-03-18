def palindrom():
    slovo = input("zadejte slovo a ja zjistit jestli je palindrom: ")
    slovo = slovo.replace(" ","")
    slovo_opacne = slovo[::-1]
    if slovo == slovo_opacne:
        print("je to palidnrom")
    else:
        print("neni")

def faktorial(n):
        import math
        vysledek = math.factorial(n)
        print(f"{n}! = ", end="")
        for i in range (1, n+1):
            if i == n:
                print(f"{i} = {vysledek} ", end="")
            else:
                print(f"{i} * ", end="")
def fakt():
    cislo = int(input("zadejte cislo a faktorial bum: "))
    if cislo == 1 or cislo == 0:
        vysledek = 1
        print(f"{vysledek}")
    elif cislo > 1:
        faktorial(cislo)
    else:
        cislo = abs(cislo)
        faktorial(cislo)
fakt()