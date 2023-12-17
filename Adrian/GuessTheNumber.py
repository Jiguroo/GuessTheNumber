from random import randint

print ('### Mini Game ###')
los = randint(1, 10)
odp = -1
i = 0
print('Zgadnij liczbę w przedziale od 1 do 10')

while odp  != los:
    i  += 1
    odp  = int(input("Podaj liczbę: "))
    if odp > los:
        print(' ')
        print('#### SPRÓBUJ PONOWNIE! ####')
        print('[?] Wylosowana liczba jest mniejsza od Twojej')
    elif odp < los :
        print(' ')
        print('#### SPRÓBUJ PONOWNIE! ####')
        print('[?] Wylosowana liczba jest wieksza od Twojej')
print(' ')
print('#### GRATULACJE! ####')
print("[!] Odgadłe za", i , "razem.")
