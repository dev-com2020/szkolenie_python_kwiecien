from itertools import zip_longest

matrix = [[1, 2, 3], [1, 2, 3]]

matrix_t = [list(i) for i in zip(*matrix)]

print(matrix_t)

# id = [1, 2, 3, 4]
# leaders = ['Marian', 'Tomek', 'Agata', 'Jacek']
# # plec = ['m', 'm', 'k', 'm']
#
#
# wyniki_slownik = {i: name for i, name in zip(id, leaders)}
# print(wyniki_slownik)
#
# wyniki_slownik2 = dict(zip(id, leaders))
# print(wyniki_slownik2)
#
# inne_id = [5, 6]
# inny_leaders = ['Paweł', 'Ola']
# wyniki_slownik.update(zip(inne_id, inny_leaders))
# print(wyniki_slownik)

# lista = zip_longest(id, leaders)
# lista2 = zip_longest(id)
# lista3 = zip_longest(id, leaders, plec, fillvalue='BrakID')
# print(lista)
# print(list(lista))
# # print(list(lista2))
# print(list(lista3))

# wyniki = [(1, 'Marian'), (2, 'Tomek'), (3, 'Agata'), (4, 'Jacek')]
# print(*wyniki)
# id,imie = zip((1, 'Marian'), (2, 'Tomek'), (3, 'Agata'), (4, 'Jacek'))
#
# print(id)
# print(imie)

produkty = ["jabłka", "banany", "wiśnie"]
ceny = [5, 10, 9]
koszty = [1, 3, 4]

for prod, c, k in zip(produkty, ceny, koszty):
    print(f"Profit z sprzedaży {prod} to PLN{c - k}!")
