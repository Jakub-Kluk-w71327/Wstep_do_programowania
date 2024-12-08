ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
liczba_bloków = 5
liczba_lokali = 10

adresy = []

for ulica in ulice:
    for blok in range(1, liczba_bloków + 1):
        for lokal in range(1, liczba_lokali + 1):
            adres = f"{ulica} {blok}/{lokal}"
            adresy.append(adres)

for adres in adresy:
    print(adres)