import random

class BlackJack:
    def start(self):
        start_input = input("Chcete si zahrát BlackJack o peníze? (a/n) \n").strip().lower()
        if start_input == "a":
            print("\n" * 5)
            self.main()
        else:
            print("Hra byla ukončena.")
            
    def main(self):
        karty_uzivatele = []
        for i in range (1,3):
            karty_uzivatele.append(self.random_karta())
        
        karty_pocitace = []
        for i in range(1,3):
            karty_pocitace.append(self.random_karta())
        
        while True:
            self.vypsani_karet_a_value(karty_pocitace, karty_uzivatele)

            if self.soucet(karty_uzivatele) > 21:
                print("Prohrál jsi, máš více než 21!")
                return
            elif self.soucet(karty_pocitace) > 21:
                print("Vyhrál jsi, počítač má více než 21!")
                return

            user = input("Hit nebo Stand? (hit/stand): ").strip().lower()
            if user == "hit":
                karty_uzivatele.append(self.random_karta())
            elif user == "stand":
                while self.soucet(karty_pocitace) < 17:
                    karty_pocitace.append(self.random_karta())
                    self.vypsani_karet_a_value(karty_pocitace, karty_uzivatele)
                    if self.soucet(karty_pocitace) > 21:
                        print("Vyhrál jsi, počítač má více než 21!")
                        return
                break
            else:
                print("Neplatná volba")
                return

        hodnota_uzivatele = self.soucet(karty_uzivatele)
        hodnota_pocitace = self.soucet(karty_pocitace)

        print("\nKonec hry!")
        if hodnota_pocitace > hodnota_uzivatele:
            print("Počítač vyhrál!")
        elif hodnota_uzivatele > hodnota_pocitace:
            print("Gratuluji, vyhrál jsi!")
        else:
            print("Remíza!")

    def check_value_karty(self, karta):
        cislo = karta[:-1]  
        if cislo in ["J", "Q", "K"]:
            return 10
        elif cislo == "A":
            return 11
        else:
            return int(cislo)

    def soucet(self, karty):
        return sum(self.check_value_karty(karta) for karta in karty)

    def random_karta(self):
        karty = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        symboly = ["♠","♥","♦","♣"]
        return f"{random.choice(karty)}{random.choice(symboly)}"

    def vypsani_karet_a_value(self, karty_pocitace, karty_uzivatele):
        print("\nPočítač:")
        print(f"Karty: {karty_pocitace} | Součet: {self.soucet(karty_pocitace)}")

        print("\nUživatel:")
        print(f"Karty: {karty_uzivatele} | Součet: {self.soucet(karty_uzivatele)}\n")

blackjack_hra = BlackJack()
while True:
    blackjack_hra.start()