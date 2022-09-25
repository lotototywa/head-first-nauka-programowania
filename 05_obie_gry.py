import random
import time
gry = ['1', '2']
gra = ''
while (gra not in gry):
    gra = input('kamień, papier nozyce (1), czy trzy kubki (2) ??? ')

if gra == '1':
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

else:
    '''
    tajemnica = "czary mary"
    '''
    wybrany = ''
    kubki = ['1','2','3']
    wynik = random.choice(kubki)
    """
    początek = input('Witaj! Zagramy w trzy kubki??? [T/n] ')
    if początek == "t" or początek == "":
        time.sleep(1.5)
    if początek == tajemnica :
        print(wynik)
    """
    time.sleep(1.5)
    print('Wkładam kulkę do kubka...')
    time.sleep(1.5)
    print('Mieszam...')
    time.sleep(3)
    while(wybrany not in kubki):
        wybrany = input ('Podaj numer kubka ')
    time.sleep(1.5)
    if wynik == wybrany:
        print('Brawo!!! wygrałeś(aś) w trzy kubki !!! Gratulacje!!!')
        time.sleep(2)
        print(f'Kubek numer {wynik} przetrzymywał kulkę!!!')

    else :
        print('Niestety, nie udało ci sie wygrać')
        print(f'A prawidłową odpowiedzią był kubek numer {wynik}')