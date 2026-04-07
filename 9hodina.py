class Hodina9:
    def seznam(self):
        cisla = []
        
        print("zadejte cisla do meho seznamu")
        print("nulou ukonci zadavani")
        i = 1
        while True:
            cislo = int(input(f"zadejte {i} cislo do listu: "))
            if cislo == 0:
                break
            cisla.append(cislo)
            i += 1
        print(f"vsechna cisla: {cisla}")
        print("nejvetsi cislo", max(cisla))
        print("nejmensi cislo", min(cisla))
        print("pocet cisel", len(cisla))

    def seznam2(self):
        cisla = []
        cisladel = []
        cisladel2 = []

        mini = None
        maxi = None

        print("zadejte cisla do meho seznamu")
        i = 1
        while True:
            cislo = int(input(f"zadejte {i} cislo do listu: "))
            if cislo == 0:
                break
            cisla.append(cislo)
            i += 1

            if (mini == None) and (maxi == None):
                mini = maxi = cislo

            if cislo > maxi:
                maxi = cislo
            if cislo < mini:
                mini = cislo

        print(f"max: {maxi} - mini: {mini}: ", maxi - mini)
        
        vstup = int(input("zadejte delitele a potom odstranim cisla: "))

        for i in range(0, len(cisla)):
            if cisla[i] % vstup == 0:
                cisladel.append(cisla[i])
            else:
                cisladel2.append(cisla[i])

        print(f"seznam s pouze delitelnymi cislami s {vstup}: {cisladel}")
        print(f"seznam ktery nejsou delitenly cisla s tim {vstup}: {cisladel2}")

program = Hodina9()

program.seznam2()
#program.seznam()