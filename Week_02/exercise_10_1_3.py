from sys import exit

number = int(input('Enter the number and the program will check if this is the first number: '))

if number <= 1 or number == 4:
    print(f'The number {number} is not the first number')
else:
    for i in range(2, number // 2):
        if number % i == 0:
            print(f'The number {number} is not the first number')
            exit(0)
    print(f'The number {number} is the first number')
