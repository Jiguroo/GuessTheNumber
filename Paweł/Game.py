from random import randint

los = randint(1,10)
x=-1
i =0
print('Zgadnij liczbe z zakresu 1- 10 ')

while x != los:
    i+=1
    x = int(input ('Podaj liczbe: '))
    if x > los:
        print ('Wylosowana liczba jest mniejsza od Twojej ')
    if x <los:
        print('Wylosowana liczba jest wieksza od Twojej ')
        
print ('Brawo odgadles, zajelo ci to {} prób'.format(i))
