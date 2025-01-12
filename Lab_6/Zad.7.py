import numpy as np

def negacja_binarna(matrix):
    return np.logical_not(matrix).astype(int)


matrix = np.zeros((5,5))

matrix[0,:] = 1 #gorny_brzeg
matrix[:,0] = 1 #lewy_brzeg
matrix[:,4] = 1 #prawy_brzeg
matrix[4:,:] = 1 #dolny_brzeg

print('Tablica po wypełnieniu jedynkami na każdej krawędzi:')
print(matrix)
print('\n')

print('Odwrócenie logiczne wartości macierzy:')
print(negacja_binarna(matrix))