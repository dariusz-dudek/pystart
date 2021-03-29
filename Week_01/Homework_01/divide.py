print('Program oblicza czy podana liczba jest podzielna przez 5, 11 lub przez 5 i 11')
number = int(input('Podaj liczbę całkowitą: '))

if number % 5 == 0 and number % 11 == 0:
    print('Podana liczba jest podzielna przez 5 i przez 11')
elif number % 5 == 0:
    print('Podana liczba jest podzielna przez 5')
elif number % 11 == 0:
    print('Podana liczba jest podzielna przez 11')
else:
    print('Podana liczba nie jest podzielna ani przez 5 ani przez 11')
