import random

zwyciezca = ''
opcje = ['kamień', 'papier', 'nozyce']
wybor_komputera = random.choice(opcje)

wybor_uzytkownika = ''

while (wybor_uzytkownika not in opcje):
    wybor_uzytkownika = input('kamień, papier czy nozyce? ')

if wybor_uzytkownika == wybor_komputera:
    zwyciezca = 'Remis'
elif wybor_komputera == 'kamień' and wybor_uzytkownika == 'nozyce':
    zwyciezca = 'Komputer'
elif wybor_komputera == 'papier' and wybor_uzytkownika == 'kamień':
    zwyciezca = 'Komputer'
elif wybor_komputera == 'nozyce' and wybor_uzytkownika == 'papier':
    zwyciezca = 'Komputer'
else:
    zwyciezca = 'Uzytkownik'

if zwyciezca == 'Remis':
    print(f'Obaj wybraliśmy {wybor_komputera}, zagraj ponownie.')
else:
    print(f'Wygrał {zwyciezca}. Komputer wybrał {wybor_komputera}.')