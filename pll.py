# import asyncio  # Importujemy moduł asyncio.
# import time  # Importujemy moduł time.
#
# print("Mój drugi program asynchroniczny.")
# print()
#
#
# async def poinformuj(opóźnienie, komunikat):
#     print(f"Przed: {komunikat}")  # Początkowy pomiar czasu.
#     await asyncio.sleep(opóźnienie)  # Usypianie wykonania programu.
#     print(f"Po: {komunikat}")
#
#
# async def main():  # Definicja asynchronicznej funkcji o nazwie main().
#     print(f"Start: {time.strftime('%X')}.")  # Końcowy pomiar czasu.
#     task1 = asyncio.create_task(poinformuj(1, "Pierwsze zadanie zostało uruchomione."))
#     task2 = asyncio.create_task(poinformuj(2, "Drugie zadanie zostało uruchomione."))
#     await task1  # Wstrzymanie wykonywania zadania 1 na jedną sekundę.
#     await task2  # Wstrzymanie wykonywania zadania 2 na dwie sekundy.
#     print(f"Stop: {time.strftime('%X')}.")
#
#
# asyncio.run(main())  # Wywołanie funkcji main().

import asyncio  # Importujemy moduł asyncio.


async def mnożenie(pierwszy, drugi):

    print(f"Obliczanie iloczynu {pierwszy} x {drugi}", ".", sep="")
    await asyncio.sleep(1)
    iloczyn = pierwszy * drugi
    print(f"Wynik: {iloczyn}", ".", sep="")


async def dodawanie(pierwszy, drugi):

    print(f"Obliczanie sumy {pierwszy} + {drugi}", ".", sep="")
    await asyncio.sleep(1)
    suma = pierwszy + drugi
    print(f"Wynik: {suma}", ".", sep="")


async def main(pierwszy, drugi):  # Definicja asynchronicznej funkcji

        print("Program asynchronicznie oblicza sumę i iloczyn dwu liczb.")
        print()
        await dodawanie(pierwszy, drugi)
        print()
        await mnożenie(pierwszy, drugi)

asyncio.run(main(50, 90))  # Wywołanie funkcji main().
