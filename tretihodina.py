def horskadraha():
    while(True):
        try:
            vyska = int(input("zadejte vysku: "))
            break
        except:
            print("zadej realny cislo")
    while(True):
        try:
            vek = int(input("zadejte vek: "))
            break
        except:
            print("zadej realny cislo")

    penize = 0

    if vyska <= 87:
        print("bohuzel nesmite")
    else:
        if vek <= 0:
            print("neexistujete pane/ní")
        else:
            if vek <= 12:
                penize += 50
            elif vek <= 18:
                penize += 100
            else:
                penize += 150
        
            string = input("chcete foto ano/ne: ")
            if string == "ano":
                penize += 40
        
            print("bude vas to stat ", penize)

def cykl():
    slovicko = input("slovo: ")
    for letter in slovicko:
        print(letter)


def hadanicislo():
    a = int(input("zadejte odkud"))
    b = int(input("zadejte dokud"))
    import random
    cisel = b
    pokus = 0
    randomnum = random.randint(a,b+1)
    
    print(f"zkuste uhodnout cislo {a}-{b}")
    while(True):
        userinput = int(input("odhad: "))
        if userinput == randomnum:
            print("wow vyhral jsi")
            print(f"zandal jsi to na {pokus}. pokus")
            break
        else:
            cisel -= 1
            pokus += 1
            print("zkus to znovu")
            print(f"jeste {cisel} cisel")
        
hadanicislo()