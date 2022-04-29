# print("---Program powitanie---\n")
# imie = input("Jak masz na imię? ")
# print("Cześć", imie)
# input("Wcisnij ENTER aby zakończyć")
#

# napis = "Matematyka jest królową nauk"
# print((napis.upper()).count("A"))
#
# tekst = "Matematyka AAA jest królową wszystkich nauk"
#
# ile = 0
# for i in tekst:
#     if i == "a" or i == "A":
#         ile += 1
# print(ile)
#
# tekst = "Matematyka jest królową wszystkich nauk"
# print("ilość wystąpień: ", tekst,)
# print()
# liczba = 0
# for literka in tekst:
#     if literka == "A" or literka == "a":
#         liczba += 1
# print("Liczba wystąpień", liczba)
#
# matematyka = "Matematyka jest królową wszystkich nauk"
# print(matematyka.count("a"), matematyka.count("A"))

imiona = 'Małgorzata Jakub Bartosz Julia Max Agata'

print(imiona)

if 'Jakub' in imiona:
    print("Jakub został znaleziony")

if 'Adam' not in imiona:
    print("Adam nie został znaleziony")

# for x in range(1,10):
#     print("0" * x)
#
# for x in range(8, 0, -1):
#     print("0" * x)


import matplotlib.pyplot as plt
x = [-0.25, -0.25, -4.5, -0.5, -3, -0.5, -2, 0, 2, 0.5, 3, 0.5, 4.5, 0.25, 0.25]
y = [0, 1.5, 1.5, 2.5, 2.5, 3.5, 3.5, 4.5, 3.5, 3.5,2.5, 2.5, 1.5, 1.5, 0]

plt.fill_between(x, y, facecolor= 'green')
plt.show()