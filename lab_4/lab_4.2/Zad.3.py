name = input('Podaj imie: ')
language = input('Podaj język: ')


def powitanie(name='Użytkowniku', language='polski'):

    match(language):
        case 'polski':
            print(f'Cześć, {name}')
        case 'angielski':
            print(f'Hello, {name}')
        case 'niemiecki':
            print(f'Guten Morgen, {name}')
        case _:
            print(f'Witaj, {name}')


    return 0

powitanie(name, language)

