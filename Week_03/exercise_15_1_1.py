print('The program will add ten positive numbers and will return max and min value')

numbers = []
while len(numbers) < 10:
    number = input('Enter the positive number: ')
    if int(number) < 0:
        print('This is not positive number.')
        continue
    numbers.append(int(number))

print(f'The numbers given by the user are: {", ".join(str(number) for number in numbers)}. Min value is {min(numbers)} and max value is {max(numbers)}')



