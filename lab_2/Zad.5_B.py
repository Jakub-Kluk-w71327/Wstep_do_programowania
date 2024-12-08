with open('notowania_gieldowe.txt', 'a') as plik:
    plik.write('\nALC, 113')
with open('notowania_gieldowe.txt', 'r') as plik:
    for line in plik:
        print(line, end='')
plik.close()