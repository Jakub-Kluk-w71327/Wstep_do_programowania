import random

print('Zad.6')
droga = random.randint(10,150)
srednie_spalanie = float(input('Podaj średnie spalanie twojego auta w (litrach/na 100 km): '))
cena_paliwa = float(input('Podaj aktualną cenę paliwa: '))

wynik = (droga/100)*srednie_spalanie*cena_paliwa

print(f'{droga} km przejedziesz za kwotę {wynik:.2f} zł')