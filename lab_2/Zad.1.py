liczba_punktow = int(input('Podaj liczbę punktów: '))

if liczba_punktow > 80:
    print('Egzamin zaliczono w terminie 0')
elif liczba_punktow >= 50 and liczba_punktow <=80:
    print('Możesz poprawić egzamin')
else:
    print('Egzamin do poprawy')