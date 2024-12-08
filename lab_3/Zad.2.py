liczby_pierwsze = []
num = 2

while len(liczby_pierwsze) < 10:
    czy_pierwsza = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            czy_pierwsza = False
            break
    if czy_pierwsza:
        liczby_pierwsze.append(num)
    num += 1

print(", ".join(map(str, liczby_pierwsze)))