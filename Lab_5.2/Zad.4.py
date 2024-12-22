import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

pracownicy = [
    {'Id': 1, 'Imię': 'Anna', 'Nazwisko': 'Kowalska', 'Stanowisko': 'Manager', 'Wiek': 35, 'Pensja (w PLN)': 8000},
    {'Id': 2, 'Imię': 'Jan', 'Nazwisko': 'Nowak', 'Stanowisko': 'Programista', 'Wiek': 28, 'Pensja (w PLN)': 4500},
    {'Id': 3, 'Imię': 'Katarzyna', 'Nazwisko': 'Wiśniewska', 'Stanowisko': 'Konsultant', 'Wiek': 40, 'Pensja (w PLN)': 6000},
    {'Id': 4, 'Imię': 'Tomasz', 'Nazwisko': 'Kaczmarek', 'Stanowisko': 'Programista', 'Wiek': 30, 'Pensja (w PLN)': 5500},
    {'Id': 5, 'Imię': 'Michał', 'Nazwisko': 'Zieliński', 'Stanowisko': 'Manager', 'Wiek': 45, 'Pensja (w PLN)': 7000}
]

df = pd.DataFrame(pracownicy)

#a
pracownicy_pensja_powyzej_5000 = df[df['Pensja (w PLN)']>5000]
print(f'a) Oto lista osób, która zarabia powyżej 5000 PLN: \n{pracownicy_pensja_powyzej_5000}\n\n')

#b
sortowanie_wg_wieku = df.sort_values(by='Wiek', ascending=True)
print(f'b) Oto posortowana lista według wieku: \n{sortowanie_wg_wieku}\n\n')

#c
grupowanie_wg_stanowiska_avg_pensja = df.groupby('Stanowisko')['Pensja (w PLN)'].mean().reset_index()
print(f'c) Średnia pensja na każdym stanowisku \n{grupowanie_wg_stanowiska_avg_pensja}\n\n')

#d
pracownicy_nowe_stanowiska = [
    {'Id': 1, 'Stanowisko': 'Informatyk'},
    {'Id': 2, 'Stanowisko': 'Prawnik'},
    {'Id': 3, 'Stanowisko': 'Lekarz'},
    {'Id': 4, 'Stanowisko': 'Policjant'},
    {'Id': 5, 'Stanowisko': 'Strażak'}

]
df_nowe_stanowiska = pd.DataFrame(pracownicy_nowe_stanowiska)

merged_df = pd.merge(df, df_nowe_stanowiska, on='Id', suffixes=('_stare', '_nowe'))
merged_df.to_csv('pracownicy.csv', index=False)
print('Plik został zapisany poprawnie!\n\n')

test = pd.read_csv("pracownicy.csv")
print(f'Testowy odczyt pliku pracownicy.csv\n {test}')

