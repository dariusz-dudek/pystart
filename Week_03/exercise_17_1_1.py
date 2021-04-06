pessel = input('Enter the number and the program will check its correctness: ')

multipliers = 1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1

s = 0
for pes, mul in zip(pessel, multipliers):
    s += int(pes) * mul

print(f'PESSEL number {pessel} is {"" if str(s)[-1] == "0" else "is not"}correct')