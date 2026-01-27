def main():
    a = int(input("zadejte prvni cislo: "))
    znaminko = input("zadejte znaminko: +,-,/,*: ")
    b = int(input("zadejte druhe cislo: "))


    if znaminko == "+":
        vysledek = a + b
    elif znaminko == "-":
        vysledek = a - b
    elif znaminko == "/":
        vysledek = a / b
    elif znaminko == "*":
        vysledek = a * b

    print(vysledek)

if __name__ == "__main__":
    main()