n = int(input("Podaj liczbę studentów: "))

if n < 1:
    print('Brak studentów')
    exit()
suma_punktow = 0
liczba_studentow = 0

while True:
    punkty = int(input(f"Podaj punkty studenta {liczba_studentow + 1}: "))

    if punkty < 0 or punkty > 100:
        print("Wprowadzono nieprawidłową wartość.")
        continue

    suma_punktow += punkty
    liczba_studentow += 1

    if liczba_studentow == n:
        break


srednia = suma_punktow / liczba_studentow
print(f"Średnia liczba punktów w grupie labolatoryjnej wynosi: {srednia:.2f}")
