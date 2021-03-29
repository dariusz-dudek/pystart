names = ['James', 'John', 'Robert', 'Michael', 'Wiliam', 'Alexander']
longest = names[0]
shortest = names[0]

for i in names:
    if len(i) > len(longest):
        longest = i
    if len(i) < len(shortest):
        shortest = i

print(f'On the list given the longest name is {longest} and the shortest is {shortest}')