a = float(input('Podaj współczynnik a: '))
b = float(input('Podaj współczynnik b: '))

if a == 0:
    if b == 0:
        print("Nieskończenie wiele rozwiązań")
    else:
        print("Brak rozwiązań")
else:
    x = -b / a
    print(f'Rozwiązanie to: {x:.2}')