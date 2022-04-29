class Tesla:

    def __init__(self):
        self.__silnik = False
        self.__bieg = 0
        self.__predkosc = 0

    def uruchom(self):
        self.__silnik = True
        print("Włączam __silnik")

    def wylacz(self):
        self.__silnik = False
        print("Wyłączam __silnik")

    def __biegNastepny(self):
        if self.__bieg <= 6:
            self.__bieg += 1
            print("Bieg:", self.__bieg)

    def __biegPoprzedni(self):
        if self.__bieg >= 0:
            self.__bieg -= 1
            print("Bieg:", self.__bieg)

    def przyspiesz(self):
        if self.__silnik is True:
            self.__predkosc += 10
            print("Szybkosc:", self.__predkosc)
            self.__biegNastepny()

    def hamuj(self):
        if self.__predkosc >= 10:
            self.__predkosc -= 10
            print("Prędkość:", self.__predkosc)
        else:
            self.__predkosc = 0
            print("Prędkość:", self.__predkosc)
            self.__biegPoprzedni()


car = Tesla()
car.uruchom()
car.przyspiesz()
car.przyspiesz()
car.przyspiesz()
car.hamuj()
car.wylacz()
