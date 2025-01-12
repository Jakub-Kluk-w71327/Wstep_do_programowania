import matplotlib.pyplot as plt

kategorie = ['Spożywcze', 'AGD', 'Elektronika', 'Meble', 'Odzież']
sprzedaz = [200, 150, 120, 100, 80]
print(f'Kategorie: {kategorie}')
print(f'Sprzedaż: {sprzedaz}')

plt.figure(figsize=(8, 5))
plt.bar(kategorie, sprzedaz, color='cornflowerblue', edgecolor='black')
plt.title('Ilość sprzedanych produktów w różnych kategoriach', fontsize=14)
plt.xlabel('Kategorie', fontsize=12)
plt.ylabel('Ilość sprzedanych produktów', fontsize=12)

for i, value in enumerate(sprzedaz):
    plt.text(i, value + 5, str(value), ha='center', fontsize=10)

plt.tight_layout()
plt.show()
