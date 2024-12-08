def ciag_fibbonaciego(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ciag_fibbonaciego(n-1) + ciag_fibbonaciego(n-2)


n = int(input("Podaj parametr n: "))

if n > 1:
    print(ciag_fibbonaciego(n))
else:
    print('Wprowadzono nieprawidłową wartość')