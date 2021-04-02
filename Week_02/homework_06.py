from math import sqrt


def first(num):
    if num <= 1 or num == 4:
        return False
    for j in range(2, round(sqrt(num) + 1)):
        if num % j == 0:
            return False
    return True


print('The program will print on the screen primes from the value to the value \nprovided by user.')

value_from = int(input('Enter the value from: '))
value_to = int(input('Enter the value to: '))
first_numbers = []

for numbers in range(value_from, value_to + 1):
    if first(numbers):
        first_numbers.append(numbers)

print(f'The prime numbers from {value_from} to {value_to}:\n {", ".join(str(f) for f in first_numbers)}')

