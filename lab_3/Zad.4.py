liczba_gosci = int(input("Podaj liczbę gości: "))
liczba_potraw = int(input("Podaj liczbę zamówionych potraw: "))

suma_cen = 0
potrawy_licznik = 0

while potrawy_licznik < liczba_potraw:
    cena = float(input(f"Podaj cenę potrawy {potrawy_licznik + 1}: "))
    suma_cen += cena
    potrawy_licznik += 1

srednia_cena = suma_cen / liczba_potraw

rachunek = suma_cen
rachunek_na_goscia = rachunek / liczba_gosci

print(f"Średnia cena potrawy: {srednia_cena:.2f} PLN")
print(f"Całkowity rachunek do zapłaty: {rachunek:.2f} PLN")
print(f"Każdy gość zapłaci: {rachunek_na_goscia:.2f} PLN")