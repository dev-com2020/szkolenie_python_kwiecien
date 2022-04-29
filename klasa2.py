from abc import ABC, abstractmethod

class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Osiągam prędkośc max.", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def __init__(self, szybkosc=55):
        super().__init__("Bielik", szybkosc)

    def poluj(self):
        print("Tu", self.gatunek, "Rozpocząłem polowanie!")

    def wydajOdglos(self):
        print("Piiiii!")


class Kura(Ptak):

    def __init__(self, gatunek="Franka"):
        super().__init__(gatunek, 1)

    def zniesJajko(self):
        print("Tu", self.gatunek, "Znosze jajko!")

    def lataj(self):
        print("Tu", self.gatunek, "Niestety ja nie latam :(")

    def wydajOdglos(self):
        print("KOKOKOK!")


o = Orzel()
o.lataj()
o.poluj()
o.wydajOdglos()

k = Kura()
print(k.szybkosc)
k.zniesJajko()
k.lataj()
k.wydajOdglos()
