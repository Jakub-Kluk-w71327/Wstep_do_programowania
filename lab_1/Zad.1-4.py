print("Zad.1 \nA)" )

#Typ wyniku działania: 1 + 2
x = 1+2
print(f'1. {type(x)}') #<class 'int'>

#Typ wyniku działania: 1 + 4.5
x = 1+ 4.5
print(f'2. {type(x)}') #<class 'float'>

#Typ wyniku działania: 3 / 2
x = 3/2
print(f'3. {type(x)}') #<class 'float'>

#Typ wyniku działania: 4 / 2
x = 4/2
print(f'4. {type(x)}') #<class 'float'>

#Typ wyniku działania: 3 //2
x = 3//2
print(f'5. {type(x)}') #<class 'int'>

#Typ wyniku działania: -3 / 2
x = -3/2
print(f'6. {type(x)}') #<class 'float'>

#Typ wyniku działania: 11 % 2
x = 11%2
print(f'7. {type(x)}') #<class 'int'>

#Typ wyniku działania: 2 ** 10
x = 2**10
print(f'8. {type(x)}') #<class 'int'>

#Typ wyniku działania: 8 ** (1/3)
x = 8**(1/3)
print(f'9. {type(x)}\n') #<class 'float'>

print('B)')
print(f'1. {int(3.0)}') #3, float na int
print(f'2. {float(3)}') #3.0, int na float
print(f'3. {float("3")}') #3.0, string na float
print(f'4. {str(12.4)} {type(str(12.4))}') #'12.4' float na string
print(f'5. {bool(0)}') #False

print(f'\nZad.2')
uczelnia = 'Studiuję na WSIiZ'
print(uczelnia)

print(f'\nZad.3')
name = 'Jan'
age = 20
height = 178
print(f'Nazywam się {name} i mam {age} lat.\nMój wzrost to 178 cm.')

print(f'\nZad.4')
price = 39.99
discount = 0.2

final_price = price * (1-discount)
print(f'Cena wynosi: {final_price:.2f}')



