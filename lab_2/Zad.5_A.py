plik = open('notowania_gieldowe.txt', 'r')

for line in plik:
    print(line,end="")


print(plik.read())

plik.close()