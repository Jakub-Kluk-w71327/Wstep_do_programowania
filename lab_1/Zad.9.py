a = float(input('Podaj pierwszą liczbę: '))
b = float(input('Podaj drugą liczbę: '))

print(f'Wynikiem działania: {a} + {b} jest {a+b}')
print(f'Wynikiem działania: {a} - {b} jest {a-b}')
print(f'Wynikiem działania: {a} * {b} jest {a*b}')

if b != 0:
    print(f'Wynikiem działania: {a} / {b} jest {a / b}')
else:
    print(f'Działanie {a} / {b}, jest niepoprawne, gdyż b jest zerem!')

print(f'Wynikiem działania: {a} ** {b} jest {a**b}')



