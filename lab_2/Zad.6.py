print('Kody ASCII')

print(f'a: {ord("a")}')
print(f'z: {ord("z")}')

print(f'A: {ord("A")}')
print(f'Z: {ord("Z")}')

#Tutaj printuje kody ASCII.
#Robiłem kiedyś podobne zadanie w C++, więc takie rozwiązanie proponuje od siebie.

char = input('Podaj znak do sprawdzenia: ')

if len(char) == 1:
    kod_ascii = int(ord(char))

    if kod_ascii > 96 and kod_ascii < 123:
        print('Mała litera')
    elif kod_ascii > 64 and kod_ascii < 91:
        print('Duża litera')

else:
    print('Niepoprawna długość znaku')