divide_3 = set(range(3, 1000, 3))
divide_5 = set(range(5, 1000, 5))
result = divide_3 & divide_5

result = sorted(list(result))

print(f'A common part of a set of numbers divided by 3 and a set of numbers divided by 5 to a value of 1000 is {", ".join(str(value) for value in result) }')