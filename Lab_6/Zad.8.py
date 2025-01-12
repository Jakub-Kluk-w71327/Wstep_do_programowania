import numpy as np

random_matrix = np.random.randint(0, 100, (5, 5))

print('Macierz z losowymi liczbami: ')
print(random_matrix)
print('\n')

licz_liczby = 0
liczby_powyzej_20 = []

for i in range(5):
    for j in range(5):
        if(random_matrix[i,j] > 20):
            liczby_powyzej_20.append(random_matrix[i,j])

print('Liczby > 20')
liczby_powyzej_20 = np.array(liczby_powyzej_20)
print(liczby_powyzej_20)
print('\n')

print('Średnia całej tablicy:')
print(random_matrix.mean())