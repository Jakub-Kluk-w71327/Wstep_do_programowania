gol = int(input('Podaj liczbę goli: '))
bonus = 0

punkty_za_bramki = gol*10

if gol > 5:
    bonus = 5
if gol > 10:
    bonus = 10

#a)
print(f'a) Całkowity wynik wynosi: {punkty_za_bramki+bonus}')