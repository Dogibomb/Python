def kalkulacka():
    vstup = str(input("zadejte priklad: "))
    vysledek = eval(vstup)

def kalkulackanormalni() -> int:
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
    else:
        vysledek = "neznam toto znaminko"

    return vysledek
def kalkulackavypsani():
    vysledek = kalkulackanormalni()
    print("vysledek je: ",vysledek)

def kamennuzkylogika() -> str:
    import random
    pocitac = random.randint(1, 3)
    

    if pocitac == 1:
        pocitac = "kamen"
    elif pocitac == 2:
        pocitac = "nuzky"
    elif pocitac == 3:
        pocitac = "papir"
    
    while True:
        clovek = input("zadejte kamen, nuzky  nebo papir: ")
        if (clovek != "kamen") and (clovek != "nuzky") and  (clovek != "papir"):
            print("spatne")
        else:
            break

    print("pocitac: ",pocitac)
    print("           vs")
    print("hrac:    ",clovek)

    if clovek == "kamen":
        if pocitac == "kamen":
            vysledek = "remiza"
        elif pocitac == "nuzky":
            vysledek = "vyhra"
        elif pocitac == "papir":
            vysledek = "prohra" 
    elif clovek == "nuzky":
        if pocitac == "kamen":
            vysledek = "prohra"
        elif pocitac == "nuzky":
            vysledek = "remiza"
        elif pocitac == "papir":
            vysledek = "vyhra" 
    elif clovek == "papir":
        if pocitac == "kamen":
            vysledek = "vyhra"
        elif pocitac == "nuzky":
            vysledek = "prohra"
        elif pocitac == "papir":
            vysledek = "remiza" 
    
    return vysledek

def kamennuzky():
    bodypocitace = 0
    bodyhrace = 0
    while True:
        vysledek = kamennuzkylogika()
        print("")
        print("hráč: ",vysledek)
        if vysledek == "vyhra":
            bodyhrace += 1
        elif vysledek == "prohra":
            bodypocitace += 1
        else:
            print("remiza nikomu nejdou body :(")

        print("body hrace: ",bodyhrace)
        print("body pocitace: ", bodypocitace)

        if bodypocitace == 3:
            print("vyhral proti tobe pocitac")
            break
        elif bodyhrace == 3:
            print("vyhral jsi nad pocitacem gratuluju")
            break
def mainkalkulacka():
    rozhdonuti = int(input("chces hrat kamen nuzky?: 1 nebo 2: "))
    if rozhdonuti == 1:
        kamennuzky()
    elif rozhdonuti == 2:
        print("okay")
    else:
        print("to neni na vyber")

mainkalkulacka()