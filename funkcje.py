def witajProgramisto():
    print("Witaj!")


def ksero(tekst="Tomek", ile=1):
    return (tekst + " ") * ile


def duzo(tekst="", **kwargs):
    print(tekst + "!")
    # print(args)
    print(kwargs)


ilosc = 0
imie = "Tomek"

# witajProgramisto()
# wynik = ksero(ile=3, tekst="Janek")
# print(wynik)

# duzo("Tomek")
a = 2


def globalna():
    global a
    a = 1
    b = 2
    return a + b


def nieglobalna():
    # a = 3
    c = 3
    return a + c


#
# print(globalna())
# print(nieglobalna())


def srednia_oceny(oceny):
    if type(oceny) is not list:
        return f"Zbyt mało danych!:{type(oceny)}"
    srednia = sum(oceny) / len(oceny)
    return round(srednia, 2)


def srednia_oceny2(oceny):
    if type(oceny) is not list:
        return f"Zbyt mało danych!:{type(oceny)}"
    suma = sum(oceny)
    if oceny.count(5) > 4 or oceny.count(6) > 4:
        suma += 4
    srednia = suma / len(oceny)
    return round(srednia, 2)


print(srednia_oceny2([2, 3, 3, 4, 5, 3, 4, 2, 1]))
print(srednia_oceny2([5, 5, 5, 1, 2, 1]))
print(srednia_oceny2([5, 5, 5, 5, 5]))
