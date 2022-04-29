# data = '27/04/2022'
# lista_daty = data.split('/')
# print(lista_daty)
# print("Miesiąc:",lista_daty[1])
#
import pickle

slownik = {'Magdalena': '500100200',
           'Jakub': '501101201',
           'Sławomir': '503111200',
           'Bartosz': '500300200'}

print("Serializacja...")
plik_wejsciowy = open("info.dat", "wb")
pickle.dump(slownik, plik_wejsciowy)
plik_wejsciowy.close()
print("DeSerializacja...")

plik_wyjsciowy = open("info.dat", "rb")
koniec_pliku = False

while not koniec_pliku:
    try:
        slownik1 = pickle.load(plik_wyjsciowy)
        print("Wydruk z pliku binarnego:", slownik1)
    except EOFError:
        koniec_pliku = True

plik_wyjsciowy.close()

#
# for klucz, wartosc in slownik.items():
#     print(klucz, wartosc)

# wartosc = slownik.get('Jakub', 'Nie ma takiego elementu')
# print(wartosc)
# wartosc = slownik.get('Tomek', 'Nie ma takiego elementu')
# print(wartosc)

#
# zbior = set()
# print("Liczba elementów:", len(zbior))
# zbior.add(1)
# print("Liczba elementów:", len(zbior))
# zbior.update([2, 3, 4, 5])
# print("Liczba elementów:", len(zbior))
# print(zbior)

# zbior1 = set([1, 2, 3, 4, 5])
# zbior2 = set([5, 5.5, 6.5, 7.5, 8.5])
#
# zbior = zbior1.union(zbior2)
# print(zbior)
