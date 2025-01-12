import numpy as np

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

wagi = np.array([128, 64, 32, 16, 8, 4, 2, 1])
print(f'Wagi: {wagi}')

liczba_bin = np.random.randint(0, 2, size=8)
print(f'Liczba binarna: {liczba_bin}')

wartosc = wartosc_liczby_bin(wagi, liczba_bin)
print(f'Wartość liczby w systemie dziesiętnym: {wartosc}')
