import numpy as np

matrix = np.random.randint(1, 100, size=(5, 5))
print('Macierz:')
print(matrix)
print('\n')

najwiekszy_element = matrix.max()
print(f'Największy element w macierzy: {najwiekszy_element}')

najmniejszy_element = matrix.min()
print(f'Najmniejszy element w macierzy: {najmniejszy_element}')

najwieksze_w_wierszach = matrix.max(axis=1)
print(f'Największe elementy w każdym wierszu: {najwieksze_w_wierszach}')

najwieksze_w_kolumnach = matrix.max(axis=0)
print(f'Największe elementy w każdej kolumnie: {najwieksze_w_kolumnach}')

suma_w_wierszach = matrix.sum(axis=1)
print(f'Suma wartości w poszczególnych wierszach: {suma_w_wierszach}')