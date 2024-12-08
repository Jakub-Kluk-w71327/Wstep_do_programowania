def czesc_wspolna(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)

    print(set1)
    print(set2)

    wspolne = list(set1 & set2)

    return wspolne

seq1 = [1,2,3,4,5]
seq2 = [4,5,6,7,8]

print(czesc_wspolna(seq1,seq2))