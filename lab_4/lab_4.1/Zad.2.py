names = ['Alan', 'Bartek', 'Kacper', 'Mateusz']
names.sort()
print(names)

names.append('Adam')
names.append('Krystian')
print(names)
print(names.pop())

names.insert(2, 'Karol')
print(names)

names.reverse()
names = names * 2
print(names)
