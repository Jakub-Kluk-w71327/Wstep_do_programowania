import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

studenci = [
    {'Nr. albumu': 1, 'Imię': 'Anna', 'Nazwisko': 'Kowalska', 'Ocena': 4.5, 'Wiek': 22},
    {'Nr. albumu': 2, 'Imię': 'Jan', 'Nazwisko': 'Nowak','Ocena': 3.0, 'Wiek': 21},
    {'Nr. albumu': 3, 'Imię': 'Katarzyna', 'Nazwisko': 'Wiśniewska','Ocena': 2.5, 'Wiek': 24},
    {'Nr. albumu': 4, 'Imię': 'Tomasz', 'Nazwisko': 'Kaczmarek','Ocena': 4.5, 'Wiek': 23},
    {'Nr. albumu': 5, 'Imię': 'Michał', 'Nazwisko': 'Zieliński','Ocena': 2.5, 'Wiek': 25},
]

df = pd.DataFrame(studenci)

#a
ocena_pow_4 = df[df['Ocena']>4.0]
print(f'a) Oto lista osób, które uzyskały ocenę wyższą, niż 4.0 \n{ocena_pow_4}\n\n')

#b
sortowanie_wg_wieku = df.sort_values(by='Wiek', ascending=True)
print(f'b) Oto posortowana lista studentów według wieku: \n{sortowanie_wg_wieku}\n\n')

#c
grupowanie_wg_avg_ocen = df.groupby('Ocena')['Wiek'].mean().reset_index()
print(f'c) Średnia wieku w każdej grupie ocenowej to: \n{grupowanie_wg_avg_ocen}\n\n')

#d
oceny_poprawa = [
    {'Nr. albumu' : 1, 'Ocena' : 4.0},
    {'Nr. albumu' : 2, 'Ocena' : 5.0},
    {'Nr. albumu' : 3, 'Ocena' : 5.0},
    {'Nr. albumu' : 4, 'Ocena' : 2.0},
    {'Nr. albumu' : 5, 'Ocena' : 3.0}

]
df_poprawa = pd.DataFrame(oceny_poprawa)

df = pd.merge(df, df_poprawa, on='Nr. albumu', suffixes=('_I termin', '_II termin'))

print(f'd) Poniższy DataFrame przedstawia tabelę zawierającą oceny z I i II terminu \n{df}\n')

print('Próba zapisu Nowego DataFrame do pliku...\n')

#e
try:
    df.to_csv('studenci.csv', index=False)
    print('Plik został zapisany poprawnie!\n')
#f
    test = pd.read_csv('studenci.csv')
    print(f'Testowy odczyt pliku pracownicy.csv\n {test}\n')
except:
    print('Coś poszło nie tak :(')

#g
df.loc[len(df)] = {'Nr. albumu': 6, 'Imię': 'Marek', 'Nazwisko': 'Nowakowski', 'Ocena_I termin': 3.5, 'Wiek': 21,'Ocena_II termin': 4.5}

#h

wartosci_unikalne = df['Ocena_II termin'].unique()
print(f'Wartości unikalne w kolumnie Ocena_II termin to: {wartosci_unikalne}\n')

#i
liczba_ocen_5 = (df['Ocena_II termin'] == 5.0).sum()
print(f'W tym DataFrame {liczba_ocen_5} osoby mają ocenę 5.0')
