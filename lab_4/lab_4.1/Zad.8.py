ranks = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)


count_ranks = len(ranks)
major_index = ranks.index("Major")
pulkownik_apperance = "Pułkownik" in ranks

print(f'W tej liście występuje {count_ranks} stopni wojskowych')
print(f'Element "Major" występuje na indexie {major_index}')
print(f'Czy element "Pułkownik" występuje?: {pulkownik_apperance}')
