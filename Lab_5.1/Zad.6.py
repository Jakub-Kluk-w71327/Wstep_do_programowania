import time

try:
    czas_uzytkownika = int(input('Podaj liczbę sekund: '))
    while czas_uzytkownika > 0:
        print(f'Pozostało {czas_uzytkownika} sekund')
        czas_uzytkownika -= 1
        time.sleep(1)
    print('Czas minął!')

except:
    print('Błędna deklaracja czasu')

