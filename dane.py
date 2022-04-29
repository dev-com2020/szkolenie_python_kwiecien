import pandas as pd

a = pd.Series([-1, 1, 3, 5, 7])
a.index = ['Pierwsza', "Druga", "Trzecia", "Czwarta", "Piąta"]
# print(a)
# print(a.describe())

b = [['Agata', 24], ['Tomek', 34], ['Andrzej', 43], ['Adam', 32]]
df_b = pd.DataFrame(b)
df_b.columns = 'Imię', 'Wiek'
# print(df_b)

c = {'Imię': ['Ewa', 'Michał', 'Krzysiek', 'Kasia', 'Lucja'],
     'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Poznań', 'Łódź']}
df_c = pd.DataFrame(c)
# print(df_c)

df = pd.read_csv('Countries.csv')
# print(df[:3])
# print(df[['Country', 'Region']])
# print(df.iloc[0:3,0:3])
# print(df.loc[:3, ['Country', 'Region', 'Population']])

df_pop = df[['Country', 'Region', 'Population', 'Phones per 1000']].copy()
print(df_pop)
