class BlackJack:
    def main(self):

        print("\n Počítač: \n") 
        karty_pocitace = []
        for i in range(1,3):
            karty_pocitace.append(self.random_karta())
        value_pocitac = 0
        for i in karty_pocitace:
            value_pocitac += self.check_value(i)
        
        print(f"karty Počítače: \n{karty_pocitace}")
        print(f"Součet: {value_pocitac}")
        

        print("\n Uživatel: \n")
        karty_uzivatele = []
        for i in range (1,3):
            karty_uzivatele.append(self.random_karta())
        value_uzivatele = 0
        for i in karty_uzivatele:
            value_uzivatele += self.check_value(i)
        
        print(f"Vaše karty: \n{karty_uzivatele}")
        print(f"Součet: {value_uzivatele}")
        
        user = input("Hit nebo stand: ")

        if user == "Hit":
            karty_uzivatele.append(self.random_karta())
        else:
            karty_pocitace.append(self.random_karta())
        
        self.vypsani_karet_a_value(karty_pocitace, karty_uzivatele, value_pocitac, value_uzivatele)
        



    def check_value(self, cislo):
        if cislo[0] == "J":
            value = 10
        elif cislo[0] == "K":
            value = 10
        elif cislo[0] == "Q":
            value = 10
        elif cislo[0] == "A":
            value = 11
        elif "10" in cislo:
            value = 10
        else:
            value = cislo[0]

        value = int(value)

        return value
    def random_karta(self):
            karty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q", "A"]
            symboly = ["♠","♥","♦","♣"]

            import random

            cislo = random.choice(karty)

            symbol = random.choice(symboly)

            karta = f"{cislo}{symbol}"

            return karta
    def vypsani_karet_a_value(self, karty_pocitace, karty_uzivatele, value_pocitac, value_uzivatele):
        print("\n Počítač: \n") 
        for i in karty_pocitace:
            value_pocitac += self.check_value(i)
        
        print(f"karty Počítače: \n{karty_pocitace}")
        print(f"Součet: {value_pocitac}")
        

        print("\n Uživatel: \n")
        for i in karty_uzivatele:
            value_uzivatele += self.check_value(i)
        
        print(f"Vaše karty: \n{karty_uzivatele}")
        print(f"Součet: {value_uzivatele}")

    def start(self):
        start_input = input("Chcete si zahrat o BlackJack O Peníze a/n \n")
        if start_input == "a":
            print("\n"*99)
            self.main()
    

    
        
    



blackjack_hra = BlackJack()
blackjack_hra.start()