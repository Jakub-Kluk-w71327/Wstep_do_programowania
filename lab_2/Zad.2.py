x = float(input('Podaj x: '))
y = float(input('Podaj y: '))
z = float(input('Podaj z: '))

if x <= y and x <= z:
    najmniejszy = x

    if y <= z:
        sredni = y
        najwiekszy = z
    else:
        sredni = z
        najwiekszy = y

elif y <= x and y <= z:
    najmniejszy = y

    if z <= x:
        sredni = z
        najwiekszy = x
    else:
        sredni = x
        najwiekszy = z

else:
    najmniejszy = z

    if x <= y:
        sredni = x
        najwiekszy = y
    else:
        sredni = y
        najwiekszy = x

print(f'Kolejność liczb od najmniejszej do najwększej to: {najmniejszy}, {sredni}, {najwiekszy}')