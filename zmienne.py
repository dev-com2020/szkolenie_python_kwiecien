# import random
#
# zakupy = [532587458, "mleko", 5.99, "chleb"]
# print(zakupy[-1])
# lista2 = [11, 2, 223, 4, 25]
# # lista = [zakupy + lista2]
# zakupy.extend(lista2)
# # print(lista[0][1])
# lista2.sort()
# lista2.reverse()
# print(lista2)
# zakupy.append("Cola")
# zakupy.insert(0, 587488565)
# # zakupy[0] = 123456789
# zakupy.pop(2)
# print(zakupy)
# print(len(zakupy))
# print("chleb" in zakupy)
#
# wyniki = []
# wyniki = list(range(1000, 1010, 5))
# print(wyniki)
#
# oceny = []
# oceny.append(random.randint(1, 100))
# print(oceny)
#
# swiatla = ("czerwony", "żółty", "zielony")
# swiatla2 = ("niebieski", "biały", "różowy")
# swiatla3 = swiatla + swiatla2
# print(swiatla3)
#
# zm = 5, 6, 7
# print(zm)
# x, y, z = zm
#
# oceny = {6, 3, 1, 2, 6, 5}
# oceny2 = {6, 3, 4, 1, 2, 6, 5}
# print(oceny2 - oceny)
# print(oceny2.difference(oceny))
# print(oceny2.intersection(oceny))
# print(oceny2 & oceny)
# print(oceny2 | oceny)
#
# imiona = {"Tomek", "Ania", "Michał", "Tomek"}
# print(imiona)
# print(oceny)
#
# slownik = {1: "Tomek", 2: "Janek", 3: "Agata"}
# slownik[4] = "Artur"
# print(slownik[4])
# print(slownik.keys())
# print(slownik.values())
# print(4 in slownik.keys())

# imiona = ['Jakub', 'Bartosz', 'Max', 'Agata']
# print("Pierwsza wersja:", imiona)
#
# imie = input("Podaj imię do usunięcia:")
# imie_index = imiona.remove(imie)
#
# print("Druga wersja:", imiona)


# lista = [12, 58, 22, 36, 102, 5]
# print("Najmniejsza:", min(lista))
# print("Największa:", max(lista))
# print("Suma:", sum(lista))
# print("Średnia wartość:", sum(lista)/len(lista))


# for i in range(-2, -10, -2):
#     print(i)

# liczba1 = 2
# liczba2 = 2
#
# if liczba1 > liczba2:
#     print("Pierwsza większa")
# elif liczba1 < liczba2:
#     print("Druga większa")
# else:
#     print("Obie są równe!")

# liczba = input("Podaj liczbę:")
# liczba = int(liczba)
#
# if liczba < 10:
#     print("To jest mała liczba")
# elif 9 < liczba < 100:
#     print("To liczba mniejsza od 100 ale więszka od 9")
# else:
#     print("To coś powyżej 100")

#
# zbior = [1, 3, 5, 7, 9]
# for index, wartosc in enumerate(zbior):
#     print(str(index) + " -> " + str(wartosc))
#
# #
# if liczba not in zbior:
#     print("Podana liczba nie znajduje się w zbiorze")

# licznik = 0
# while True:
#     licznik += 1
#     print(licznik)
#     if licznik > 10:
#         break
#
# lista = []
# print("Podaj liczby, które chcesz wstawić do listy, napisz 'x' aby zakończyć")
# while True:
#     wejscie = input()
#     if wejscie == 'x':
#         break
#     lista.append(int(wejscie))
# print("Twoja lista: ", lista)

# licznik = 0
# while licznik < 5:
#     print(str(licznik) + " mniejszy od 5")
#     licznik += 1

# x = [i for i in range(5)]
# print(x)
#
# y = [i for i in range(10) if i % 2 == 0]
# print(y)
#
# fake_liczby = ["1", "3", "5"]
# liczby = [int(i) for i in fake_liczby]
# print(liczby)
#
# oceny = [1, 2, 3, 4, 4, 5, 6]
# zbior = {i for i in oceny}
# print(zbior)
#
# slownik = {1: "Tomek", 2: "Max", 3: "Agata"}
# print({value: key for key, value in slownik.items()})

#
# test_object = 23
# print(f"test dla wartości = {test_object}")
# if test_object < 20:
#     print("Niska wartość")
# if test_object < 30:
#     print("Mniej niż 30")
# if test_object < 40:
#     print("Mniej niż 40")

#
# test_object = 23
# print(f"test dla wartości = {test_object}")
# if test_object < 40:
#     print("Mniej niż 40")
#     if test_object < 20:
#         print("Niska wartość")
#         if test_object < 30:
#             print("Mniej niż 30")


test = ["Tomek", "Agata", "Max", "Robert"]

for e in test:
    if e[0] == "T" or e[0] == "M":
        print(f"Pierwsza litera znaleziona! w {e}")
        continue
    print(f"Sprawdzam pierwszą literę w: {e}")
print("==KONIEC==")
