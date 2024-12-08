shopping_list = {
    'milk': 5,
    'eggs': 12,
    'bread': 6,
    'apples': 2,
    'butter': 7,
    'cheese': 4
}
total_cost = 0

for product, price in shopping_list.items():
    print(product, price)
    total_cost += price


print(f'Łączny koszt zakupów wynosi {total_cost} złotych.')