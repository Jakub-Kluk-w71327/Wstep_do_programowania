n = int(input("Podaj liczbę studentów: "))

if n < 1:
    print('Brak studentów')
    exit()#kończenie całego programu

suma_punktow = 0
liczba_studentow = 0

while liczba_studentow < n:
    punkty = int(input(f"Podaj punkty studenta {liczba_studentow + 1}: "))

    if punkty < 0 or punkty > 100:
        print("Wprowadzono nieprawidłową wartość.")
        continue

    suma_punktow += punkty
    liczba_studentow += 1

srednia = suma_punktow / liczba_studentow
print(f"Średnia liczba punktów w grupie labolatoryjnej wynosi: {srednia:.2f}")
