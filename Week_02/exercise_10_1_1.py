numbers = [_ for _ in range(100)]

counter_4 = 0
counter_5 = 0

for i in numbers:
    if i % 4 == 0:
        counter_4 += 1
    if i % 5 == 0:
        counter_5 += 1

print(f'In the list given to the numbers, dived by 4 is {counter_4} and dived by 5 is {counter_5}')
