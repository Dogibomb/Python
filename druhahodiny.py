#priklad 1
"""
sirka = float(input("zadejte sirku hriste: "))
delka = float(input("zadejte delku hriste: "))
kola = int(input("zadejte pocet kol: "))

jedno_kolo = 2*(sirka+delka)
celkove_ubehnu = jedno_kolo * kola

print("sirka hriste je", sirka , "metru a delka je", delka , "metru")
print("jedno kolo je", jedno_kolo, "metru")
print("po", kola, "kolech ubehnu", celkove_ubehnu, "metru")
"""

#priklad 2

"""
cena = int(input("zadejte cenu knihy: "))
sleva = int(input("zadejte slevu v %: "))

vypocet = cena - (cena *sleva/100)
slevakc = cena*sleva/100
print("cena: ", cena)
print("sleva je ", sleva, "% a to je ", slevakc, "kc")
print("zaplatis: ", vypocet)
"""

#priklad 3

"""
teplota = float(input("zadejte stupne celsia: "))

if teplota<=20:
    print("je zima")
else:
    print("je teplo")
"""

#priklad 4

"""
while(True):
    cislo = int(input("zadejte cislo: "))
    cislo = str(cislo)
    print("cislo je", len(cislo), "ciferne")
"""

#priklad 5

while(True):
    heslo = input("zadejte heslo: ")
    heslo_znovu = input("zadejte heslo znovu: ")

    if heslo != heslo_znovu:
        print("hesla se neshoduji")
    else:
        if len(heslo) >= 8:
            print("heslo je dobre")
        else:
            print("heslo je moc male")