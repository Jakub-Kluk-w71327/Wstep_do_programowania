import matplotlib.pyplot as plt

czas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
predkosc = [0, 5, 15, 20, 25, 30, 35, 40, 38, 36, 35]
print(f'Czas (s): {czas}')
print(f'Prędkość (m/s): {predkosc}')

plt.figure(figsize=(8, 5))
plt.scatter(czas, predkosc, color='red', edgecolor='black')
plt.title('Zależność prędkości od czasu', fontsize=14)
plt.xlabel('Czas (s)', fontsize=12)
plt.ylabel('Prędkość (m/s)', fontsize=12)
plt.grid(True)

plt.tight_layout()
plt.show()