def ryba_na_haczyku():
   print('Złapałem rybe! ')

def czekaj():
    print('Czekam...')

print('Biorę robaka')
print('Zakładam robaka na haczyk')
print('Zarzucam pszynęte')

while True:
    odpowiedz = input('Czy spławik jest zanurzony pod wodą? ')
    if odpowiedz == 'tak':
        rusza_się = True
        print('złapała haczyk!')
        ryba_na_haczyku()
    elif odpowiedz == "koniec":
        exit()
    else:
        czekaj()