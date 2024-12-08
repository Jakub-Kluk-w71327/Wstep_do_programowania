import math

a = float(input('Podaj a:'))
b = float(input('Podaj b:'))
c = float(input('Podaj c:'))

delta = (b**2) - (4*a*c)

if delta < 0:
    print('Brak rozwiązań')

elif delta == 0:
    x = (-b)/2*a
    print(f'Ta funkcja kwadratowa posiada jedno rozwiązanie, które wynosi: {x}')

else:
    x_jeden = (-b - math.sqrt(delta))/(2*a)
    x_dwa = (-b + math.sqrt(delta))/(2*a)
    print(f'Ta funkcja ma następujące rozwiązania x1 = {x_jeden}, natomiast x2 = {x_dwa}')