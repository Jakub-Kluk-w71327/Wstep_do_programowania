import matplotlib.pyplot as plt

kategorie = ['Spożywcze', 'AGD', 'Elektronika', 'Meble', 'Odzież']
sprzedaz = [200, 150, 120, 100, 80]
print(f'Kategorie: {kategorie}')
print(f'Sprzedaż: {sprzedaz}')

plt.figure(figsize=(6, 6))
plt.pie(
    sprzedaz,
    labels=kategorie,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightblue', 'lightgreen', 'orange', 'gold', 'violet']
)
plt.title('Procentowy udział różnych kategorii w całkowitej sprzedaży', fontsize=14)
plt.show()