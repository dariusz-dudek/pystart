import sys

while True:
    try:
        answer = input('How much liquid was provided by the factory or press ENTER to quit: ')
        if answer == '':
            sys.exit(0)
        liquid = int(answer)
        break
    except ValueError:
        print('This is not a number. Try another time.')

bottle_volume = 330
free_space = 0.12
bottle_number = liquid // (bottle_volume * (1 - free_space))
liquid_survive = liquid % (bottle_volume * (1 - free_space))

print('The employee filled {:.0f} bottles and he survived {:.0f} ml of liquid for himself'.format(bottle_number, liquid_survive))