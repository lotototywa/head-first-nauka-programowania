import turtle

imie_psa = input('Jak się Twój pies nazywa? ')

# pytaj o wiek az dostaniesz wartośc typu int
while True:
    try:
        wiek_psa = input('Ile lat ma twój pies?? ')
        wiek_ludzki = int(wiek_psa) * 7
        break
    except:
        print("Wiek psa musi być liczbą całkowitą")
        continue

print(f'twój pies {imie_psa} miałby jako człowiek {wiek_ludzki} lat(a)')
