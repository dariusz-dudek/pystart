end = True


numbers = []
while end:

    number = input('Enter the number or type "end" to end: ')
    if number.isdecimal():
        numbers.append(int(number))
    elif number == 'end':
        end = False
    else:
        print('I don\'t understand')

product = 1

for number in numbers:
    if number % 2 == 0:
        product *= number


print(f'The product of all given numbers is {product}')
