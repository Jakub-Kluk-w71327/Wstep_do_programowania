from random import sample

zakres = []

for i in range(1,50):
    zakres.append(i)

wylosowane_liczby = sample(zakres, 6)
wylosowane_liczby.sort()

print(f'Twoje wylosowane liczby to: {wylosowane_liczby}')
