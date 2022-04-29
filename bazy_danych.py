import sqlite3

konektor = sqlite3.connect('example.sqlite')

c = konektor.cursor()
#
# c.execute("""CREATE TABLE transakcje(data TEXT, id INTEGER, cena REAL)""")
# c.execute("""INSERT INTO transakcje VALUES('2022-04-27', 2, 12.22)""")
# c.execute("""INSERT INTO transakcje VALUES('2022-04-28', 3, 232.19)""")
#
# konektor.commit()

for row in konektor.execute('SELECT * FROM transakcje ORDER BY cena'):
    print(row)

konektor.close()

