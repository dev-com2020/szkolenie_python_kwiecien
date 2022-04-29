# imiona = ('Jakub', 'Bartosz', 'Max', 'Filip')
# print(imiona)
#
# imionaL = list(imiona)
# imionaL.sort()
#
# print("wydruk listy:",imionaL)
# imiona = tuple(imionaL)
# print(imiona)

# imiona = ('Jakub', 'Bartosz', 'Max', 'Filip',)
# print(tuple(sorted(list(imiona))))
# print(sorted(imiona))
#
# text = "Lubię Pythona"
# sliced = slice(6)
# print(text[sliced])
import random
#
#
# imiona = ['Jakub', 'Bartosz', 'Max', 'Filip']
# print(random.random() * 100)
# print(random.randint(1, 6))
# print(random.choice(imiona))

# napis = input("Wprowadz tekst:")
# liczba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(napis * random.choice(liczba))


# napis = input("Podaj napis: ")
# print((napis + "\n") * random.randint(1,15))

# text = input("wpisz imię:")
#
# print((text) * random.randint(1,15))

import random
napis = input("Podaj napis: ")
for i in range(random.randint(1, 15)):
    print(napis)
