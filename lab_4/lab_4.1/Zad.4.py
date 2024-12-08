import string

sentence = input('Podaj zdanie: ')
sentence = sentence.lower()

alphabet = string.ascii_lowercase
alphabet = set(alphabet)

letters = []
unique_letters = set()

for letter in sentence:
    if letter.isalpha() and letter in alphabet:
        letters.append(letter)

for element in letters:
    unique_letters.add(element)

unique_letters = list(unique_letters)
unique_letters = sorted(unique_letters)

not_existing_chars = alphabet.difference(unique_letters)
not_existing_chars = sorted(not_existing_chars)


print(f'Wszystkie występujące litery w tym zdaniu to: {unique_letters}')
print(f'Wszystkie nie występujące litery w tym zdaniu to: {not_existing_chars}')


