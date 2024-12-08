def count_bmi(height, weight):
    bmi = (weight)/(height**2)

    match bmi:
        case bmi if bmi < 18.5:
            print('niedowaga')
        case bmi if bmi >= 18.5 and bmi <= 24.9:
            print('pożądana masa ciała')
        case bmi if bmi >= 25 and bmi <= 29.9:
            print('nadwaga')
        case bmi if bmi >= 30:
            match bmi:
                case bmi if bmi >= 30 and bmi <= 34.9:
                    print('otyłość I stopnia')
                case bmi if bmi >=35 and bmi <= 39.9:
                    print('otyłość II stopnia')
                case bmi if bmi >= 40:
                    print('otyłość III stopnia')
        case _:
            print('Wprowadzono niewłaściwe dane')


height = float(input('Podaj wzrost wyrażony w metrach (np. 1.75): '))
weight = float(input('Podaj wagę wyrażoną w kilgoramach( np. 75: '))

count_bmi(height, weight)

