name = input('Podaj imię: ')
print(f'Witaj {name}')

age = int(input('Podaj wiek: '))
print(f'Twój wiek to: {age}')

name = input('Podaj imię: ')
surname = input('Podaj nazwisko: ')
initials = name[0] + surname[0]
initials = initials.upper()
print(f'Twoje inicjały to: {initials}')

string = input('Podaj łańcuch: ')
print(string * 5)

string1 = input('Podaj pierwszy łańcuch: ')
string2 = input('Podaj drugi łańcuch: ')
string3 = string1 + string2
print(f'Połączone oba łańcuchy: {string3}')

string1 = input('Podaj pierwszy łańcuch: ')
string2 = input('Podaj drugi łańcuch: ')
both_strings = string1[:len(string1)//2] + string2[len(string2)//2:]
print(both_strings)
