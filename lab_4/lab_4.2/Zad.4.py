number_of_numbers = int(input('Podaj liczbę cyfr: '))

suma = 0

for number in range(number_of_numbers):
    suma += float(input(f'Podaj wartość nr. {number+1}: '))

srednia = suma/number_of_numbers

print(f'Twoja średnia liczb wynosi: {round(srednia,2)}')