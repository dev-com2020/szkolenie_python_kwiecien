# uchwyt2 = open(r"F:\szkolenie_python\plik.txt")

# uchwyt = open("plik.txt", "a", encoding="utf-8")
# uchwyt.write("\nZapisuję do pliku ponownie kolejny raz.")
# uchwyt.close()

with open("plik.txt", "r", encoding="utf-8") as file:
    for l in file:
        print(l)




# for linia in uchwyt:
#     print(linia)
# dane = uchwyt.read(1024)
# print(dane)
# uchwyt.close()


