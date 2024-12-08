haslo = 'pk47!jy0893!'

pass_len = int(len(haslo))

count = 0

if '!' in haslo and pass_len > 10:
    print('Hasło jest poprawne')
else:
    print('Hasło jest nie poprawne')

