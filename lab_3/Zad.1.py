paliwo_w_samolocie = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo_w_samolocie > 0:
    paliwo_w_samolocie -= paliwo_zuzyte_na_s
    czas += 1
    print(f'Pozostało {paliwo_w_samolocie} litrów paliwa, Sekunda lotu {czas}')

print("Koniec lotu")