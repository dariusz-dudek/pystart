print('Calculator to change number from the binary system to decimal system')

value_in_binary = input('Enter the number in the binary system: ')

value_in_binary_reverse = value_in_binary[::-1]

value_in_decimal = int()

for i in range(0, len(value_in_binary)):
    value_in_decimal += int(value_in_binary_reverse[i]) * 2**i

print(value_in_decimal)