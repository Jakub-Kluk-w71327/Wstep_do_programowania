import random
import math

min_wartosc_uzytkownika = int(input('Podaj dolny zakres liczbowy: '))
max_wartosc_uzytkownika = int(input('Podaj górny zakres liczbowy: '))

if min_wartosc_uzytkownika<max_wartosc_uzytkownika:

    iloczyn_liczb = 1
    losowe_10_elementow = tuple(random.randint(min_wartosc_uzytkownika,max_wartosc_uzytkownika) for x in range(10))
    print(losowe_10_elementow)

    for i in range(10):
        iloczyn_liczb *= losowe_10_elementow[i]

    srednia_geometryczna = math.pow(iloczyn_liczb, 1/10)

    print(f'Średnia geometryczna krotki wynosi ok. {round(srednia_geometryczna, 2)}')

else:
    print('Podano nieprawidłowy zakres liczbowy')

