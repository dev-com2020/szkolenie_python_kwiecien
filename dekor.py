import time


def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def glowna():
    def wewnetrzna(a, b):
        return a * b

    x = wewnetrzna(2, 3)
    return x


def funk():
    def funkWew(a, b):
        return a * b

    return funkWew


# x = funk()
# print(x(3, 3))
#
# print(glowna())
# print(wykonaj(dodaj, 2, 3))
# print(wykonaj(odejmij, 2, 3))

def deko(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "wykonywała się", koniec - start, "sek.")
        return x

    return wew


@deko
def zwyklaFunkcja(a, b):
    time.sleep(1)
    return a + b


@deko
def zwyklaFunkcja2(a, b, c):
    time.sleep(0.5)
    return a + b - c


print(zwyklaFunkcja(2, 2))
print(zwyklaFunkcja2(2, 4, 1))
