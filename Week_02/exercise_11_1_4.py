text = '12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek'

weight = int()

for i in text.split(' '):
    if i.isdecimal():
        weight += int(i)

print(f'The total weight of fruit is {weight}')
