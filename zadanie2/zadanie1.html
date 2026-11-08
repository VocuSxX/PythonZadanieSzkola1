#zadanie1

class Konto:
    def __init__(self, wlasciciel, nr_konta, saldo_poczatkowe=0.0):
        self.wlasciciel = wlasciciel
        self.nr_konta = nr_konta
        self.saldo = saldo_poczatkowe
        self.kredyt = 0.0
        self.lokata = 0.0

    def zaloz_lokate(self, kwota):
        if kwota > 0 and self.saldo >= kwota:
            self.saldo -= kwota
            self.lokata += kwota
            return True
        print("Niepowodzenie brak wystarczających środków lub blędna kwota")
        return False

    def wez_kredyt(self, kwota):
        if kwota > 0:
            self.kredyt += kwota
            self.saldo += kwota
            return True
        print("Niepowodzenie kwota kredytu nie moze byc mniejsza niz 0")
        return False

    def przelew(self, kwota, inne_konto):
        if kwota >0 and self.saldo >= kwota:
            self.saldo -= kwota
            inne_konto.saldo += kwota
            return True
        print("Niepowodzenie brak wystepowania srodkow na przelew")
        return False

    def __str__(self):
        return (f"Konto: {self.nr_konta}, Wlasiciel: {self.wlasciciel}, Saldo: {self.saldo}, Lokata: {self.lokata}PNL, Kredyt: {self.kredyt}")

class Konto_VIP(Konto):
    def __init__(self, wlasciciel, nr_konta, saldo_poczatkowe=0.0):
        super().__init__(wlasciciel, nr_konta, saldo_poczatkowe)
        self.historia = []
        self.historia.append(f"Otwarto konto VIP. Saldo początkowe: {self.saldo} PNL")

    def zaloz_lokate(self, kwota):
        x = super().zaloz_lokate(kwota)
        if x:
            self.historia.append(f"Zalozono lokate na kwate {kwota} PNL")
        else:
            self.historia.append(f"Odrzucono próbe zalozenia lokaty na kwote {kwota} PNL")
        return x

    def wez_kredyt(self, kwota):
        x = super().wez_kredyt(kwota)
        if x:
            self.historia.append(f"Zaciagnieto kredyt na kwote {kwota} PNL.")
        return x

    def przelew(self, kwota, inne_konto):
        x = super().przelew(kwota, inne_konto)
        if x:
            self.historia.append(f"Wykonano przelew na kwote {kwota} PNL na konto {inne_konto.nr_konta}")
        else:
            self.historia.append(f"Przelew nieudany")
        return x
    
    def historia_konta(self):
        print(f"Historia {self.wlasciciel}")
        for x in self.historia:
            print(f"{x}")
        print("-------------------")


konto1 = Konto("Sebastian Lecz", "1234", 3000.0)
konto2 = Konto("Monika Karaś", "4321", 2137.0)

print(konto1)
print("------")
konto1.zaloz_lokate(200)
konto1.wez_kredyt(1212)
konto1.przelew(1000, konto2)
print("-----")
print(konto1)
print("------")
print(konto2)
print("------")


konto3 = Konto_VIP("Robert Sum", "6767", 10000.0)
print(konto3)
konto3.zaloz_lokate(2500)
konto3.wez_kredyt(200)
konto3.przelew(400, konto1)
konto3.przelew(121212, konto2)
konto3.historia_konta()
print(konto3)
