def main():
    a = float(input("zadejte prvni cislo: "))
    znaminko = input("zadejte znaminko: +,-,/,*: ")
    b = float(input("zadejte druhe cislo: "))


    if znaminko == "+":
        vysledek = a + b
    elif znaminko == "-":
        vysledek = a - b
    elif znaminko == "/":
        vysledek = a / b
    elif znaminko == "*":
        vysledek = a * b

    print(vysledek)

    priklad = input("zadejte priklad: ")
    print(eval(priklad))

if __name__ == "__main__":
    main()