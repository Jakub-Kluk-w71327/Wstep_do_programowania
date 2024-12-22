import datetime

def int_to_month(miesiac):
    match miesiac:
        case 1:
            return 'Styczeń'
        case 2:
            return 'Luty'
        case 3:
            return 'Marzec'
        case 4:
            return 'Kwiecień'
        case 5:
            return 'Maj'
        case 6:
            return 'Czerwiec'
        case 7:
            return 'Lipiec'
        case 8:
            return 'Sierpień'
        case 9:
            return 'Wrzesień'
        case 10:
            return 'Październik'
        case 11:
            return 'Listopad'
        case 12:
            return 'Grudzień'
        case _:
            print('Nieprawidłowy miesiąc :(')


data_dzisiejsza = datetime.date.today()
data_laboratorium = datetime.date(2024,12,15)
data_kolokwium = datetime.date(2025,1,19)

miesiac = int_to_month(data_laboratorium.month)


print(f'Od ostatniego laboratorium minęło {data_dzisiejsza.day - data_laboratorium.day} dni. Zajęcia odbyły się w miesiącu {miesiac}.')

dni_do_kolokwium = data_kolokwium - data_dzisiejsza

miesiac = int_to_month(data_kolokwium.month)

print(f'Do kolokwium (od daty 17.12.2024) zostało: {dni_do_kolokwium.days} dni. Kolokwium zaś będzie w miesiącu {miesiac}.')