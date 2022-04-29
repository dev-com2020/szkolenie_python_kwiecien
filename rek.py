# lista = [1, 3, 7, 11, 13, 17, 22]
# cel = 17
from functools import reduce


def szukaj(lista, cel, pozycja):
    if lista[pozycja] == cel:
        print("Znalazłem na pozycji:", pozycja)
        return
    elif pozycja == len(lista) - 1:
        print("Nie znalazłem celu!")
        return
    szukaj(lista, cel, pozycja + 1)


tekst = "Moduł random umożliwia generowanie losowych liczb czy też losowych wartości z sekwencji"


def zamien(tekst, pozycja):
    if tekst[pozycja].isupper():
        tekst = tekst[0:pozycja] + tekst[pozycja].lower() + tekst[pozycja + 1:]
    else:
        tekst = tekst[0:pozycja] + tekst[pozycja].upper() + tekst[pozycja + 1:]
    if pozycja == len(tekst) - 1:
        return tekst
    return zamien(tekst, pozycja + 1)


# print(zamien(tekst, 0))

# szukaj(lista, cel, 0)

#
#
# lista = [1, 3, 4, 5, 7, 8]
#
# def funk(i):
#     if i % 2 == 0:
#         return "Parzyste"
#     else:
#         return 'Nieprzyste'
#
#
# lista = [funk(i) for i in lista]
# print(lista)


# lambda <parametry> : <wyrażenie>

# x = 5
# zmienna = lambda x, y: x + 2 - y
#
# print(zmienna(x, 3))
#
# print((lambda a, b: a + b)(3, 4))


# def funkcja(f, liczba):
#     return f(liczba)
#
#
# print(funkcja(lambda x: x + 1, 7))
# print(funkcja(lambda x: x * x, 7))


# krotka = (1, 2, 3, 4, 5, 6)
# out = open('test.txt', 'w')
# out.write(str(krotka))
# out.close()

# infile = open('test.txt', 'r')
# krotka = ()
#
# with open('test.txt') as f:
#     krotka = eval(f.read())
#     print(krotka)
#     print("Suma krotki:", sum(krotka))
#
# infile.close()
#
# print(eval("2+2"))
# print(exec('for i in range(1,3): print(i)'))

lista = [1, 3, 5, 7]

print(f"Nasza lista:{lista}\n")
print(f"MAP: {list(map(lambda _: _ * 2, lista))}")
print(f"FILTER: {list(filter(lambda _: _ > 3, lista))}")
print(f"REDUCE: {reduce(lambda x, y: x + y, lista)}")
