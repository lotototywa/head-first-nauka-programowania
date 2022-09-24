import random
import time

tajemnica = "czary mary"
kubki = ['1','2','3']
wynik = random.choice(kubki)
początek = input('Witaj! Zagramy w trzy kubki??? [T/n] ')
if początek == "t" or początek == "":
    time.sleep(1.5)
if początek == tajemnica :
    print(wynik)
    time.sleep(1.5)
print('Wkładam kulkę do kubka...')
time.sleep(1.5)
print('Mieszam...')
time.sleep(3)


wybrany = input ('Podaj numer kubka ')
time.sleep(2.5)
if wynik == wybrany:
    print('Brawo!!! wygrałeś(aś) w trzy kubki !!! Gratulacje!!!')
    time.sleep(2)
    print(f'Kubek numer {wynik} przetrzymywał kulkę!!!')

else :
    print('Niestety, nie udało ci sie wygrać')
    print(f'A prawidłową odpowiedzią był kubek numer {wynik}')

