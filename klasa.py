class Czlowiek:
    """
    Klasa która tworzy obiekt androida o wymaganych parametrach:
    @:param imie,wiek,plec
    """

    def __init__(self, imie, wiek, plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        """
        Metoda która zwraca
        :return: imię danego androida
        """
        print("Cześć, mam na imię: ", self.imie)

    def ruszaj(self):
        if self.plec == "kobieta":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def liczenie(self):
        if self.wiek < 2:
            print("Ja jeszcze nie umiem liczyć!")
        else:
            print("Co mam policzyc?")


cz1 = Czlowiek("Tomek", 39, "m")
print(cz1.imie)
cz1.przywitaj()
cz1.ruszaj()
cz1.liczenie()

cz2 = Czlowiek("Agata", 1, "kobieta")
print(cz2.imie)
cz2.przywitaj()
cz2.ruszaj()
cz2.liczenie()
