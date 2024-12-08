def potega(a,n):
    if n == 0:
        return 1
    elif n > 0:
        return a * potega(a, n - 1)
    else:
        return 1 / potega(a, -n)

a = float(input('Podaj a: '))
n = float(input('Podaj n: '))

wynik = potega(a,n)
print(f'Wynik {a} do potęgi {n} wynosi: {wynik}')