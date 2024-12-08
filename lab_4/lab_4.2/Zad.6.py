import math

a = input('Podaj bok a: ')
b = input('Podaj bok b: ')
c = input('Podaj bok c: ')

try:

    a = float(a)
    b = float(b)
    c = float(c)

    if a + b > c:
        if a + c > b:
            if b + c > a:
                s = float((a + b + c) / 2)
                pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
                print(round(pole,2))
            else:
                print('Podane wartości nie tworzą trójkąta')
        else:
            print('Podane wartości nie tworzą trójkąta')
    else:
        print('Podane wartości nie tworzą trójkąta')
except:
    print('Wprowadzono niewłaściwe dane')
