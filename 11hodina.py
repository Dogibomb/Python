class Hodina11:
    def ctverec(self):
        a = int(input("zadejte cislo: "))

        if a > 0:
            print("je to kladne cislo")
            if a % 2 == 0:
                print("je to sude cislo")
            else:
                print("je to liche cislo")

            obvod = a*4
            obsah = a * a
            print("obvod je: ", obvod)
            print("obsah je: ", obsah)
        elif a < 0:
            print("cislo je zaporne")
            a = abs(a)

            print(f"prevod z {a} metru na milimetry: {a*1000}")
        else:
            print("je to nula")

    def objem(self):
        import math
        a = int(input("zadejte polomer v metrech: "))
        objemvody = ((4/3) * math.pi * math.pow(a, 3))*1000
        print("objem zasobniku je: ", objemvody)
        print("když za den spotrebujete 5 litru")
        print("prezijete: " + str(math.floor(objemvody/5)) + " dní")

    def babicka(self):
        slepice = int(input("zadejte kolik mate slepic: "))
        kraliku = int(input("zadejte kolik mate kraliku: "))

        hlavy = slepice + kraliku
        nohy = (slepice * 2) + (kraliku * 4)

        print("hlavou je: ", hlavy)
        print("nohou je: ", nohy)

    def babicka2(self):
        hlavy = int(input("Zadejte počet hlav: "))
        nohy = int(input("Zadejte počet nohou: "))

        kraliku = (nohy - (2 * hlavy)) // 2
        slepice = hlavy - kraliku
        
        print(f"Počet slepic: {slepice}")
        print(f"Počet králíků: {kraliku}")

program = Hodina11()
program.babicka2()