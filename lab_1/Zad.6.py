print('Zad.6')
droga = float(input('Podaj jaką drogę masz do pokonania (w km): '))
srednie_spalanie = float(input('Podaj średnie spalanie twojego auta w (litrach/na 100 km): '))

cena_paliwa = 6.5

wynik = (droga/100)*srednie_spalanie*cena_paliwa

print(f'Twój szacunkowy koszt przejazdu wynosi {wynik:.2f} zł')