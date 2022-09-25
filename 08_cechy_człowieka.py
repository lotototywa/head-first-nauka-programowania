def pobierz_ceche(zapytanie, domyslna):
    pytanie = zapytanie + '[' + domyslna +']? '
    odpowiedz = input(pytanie)
    if (odpowiedz == ''):
        odpowiedz = domyslna
    print('Wybrałeś/aś:', odpowiedz)
    return odpowiedz

wlosy = pobierz_ceche('Jaki kolor włosów', 'brązowy')
wlosy_dlugosc = pobierz_ceche('Jaka długość włosów', 'krótkie')
oczy = pobierz_ceche('Jaki kolor oczu', 'niebieski')
plec = pobierz_ceche('Jaka płeć', 'kobieta')
okulary = pobierz_ceche('Okulary', 'nie')
broda = pobierz_ceche('Broda', 'nie')