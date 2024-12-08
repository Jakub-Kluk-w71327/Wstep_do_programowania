my_list = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
my_list_2 = [24, 28, 30]

print(my_list[0])
print(my_list[-1])

print(len(my_list))

print(max(my_list))
print(min(my_list))

print(sum(my_list))

print(sorted(my_list))

my_list.append(6)
print(my_list)

my_list.insert(3, 5)
print(my_list)

print(my_list.pop())

my_list.reverse()
print(my_list)

my_list_3 = my_list + my_list_2
print(my_list_3)

print(my_list * 5)

print(my_list_3[:4])
print(my_list_3[6:])
print(my_list_3[3:7:3])
print(my_list_3[::-1])
