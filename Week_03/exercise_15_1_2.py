print('Enter the numbers where each subsequent will be greater than the previous one ')

numbers = []
while True:
    number = int(input('Enter the number: '))
    if not len(numbers) == 0 and number <= numbers[-1]:
        print('The number is smaller then previous.')
        break
    numbers.append(number)

print(f'The average from numbers: {", ".join(str(number) for number in numbers)} is {sum(numbers)/len(numbers):.2f}')