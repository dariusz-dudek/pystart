from random import randint

example = [tuple(randint(1, 10) for _ in range(randint(1, 10))) for _ in range(randint(5, 10))]

print(f'Sample list: {example}\n')

print('Result:')
print('\n'.join([f'Tuple nr {nr} sum is {sum(tup)}' if len(tup) % 2 == 0 else f'Tuple nr {nr} avg is {sum(tup) / len(tup):.2f}' for nr, tup in enumerate(example, start=1) if 1 < len(tup) < 6]))
