imie = str(input('Podaj imię: '))
print(f'Witaj, {imie}')
####################################################################
wiek =  int(input('Podaj wiek: '))
print(f'Twój wiek to: {wiek}')
####################################################################
imie = str(input('Podaj imię: '))
nazwisko = str(input('Podaj nazwisko: '))
print(f'Inicjały: {imie[0].upper()+nazwisko[0].upper()}')
####################################################################
text = str(input('Podaj łańcuch znaków: '))
print(5 * (text + "\n"))
####################################################################
text1 = str(input('Podaj pierwszy łańcuch znaków: '))
text2 = str(input('Podaj drugi łańcuch znaków: '))
text_1_i_text_2 = text1 + text2
print(f"Połączony łańcuch: {text_1_i_text_2}")
####################################################################
text1 = str(input('Podaj pierwszy łańcuch znaków: '))
text2 = str(input('Podaj drugi łańcuch znaków: '))

text3 = ''

for i in range(len(text1)//2):#dzielenie całkowite
    text3 += text1[i]

print(text3)
