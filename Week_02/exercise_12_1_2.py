sentence = input('Enter the sequence: ')

dictionary = {}

for word in sentence.lower().split(' '):
    dictionary[word] = sentence.count(word)

print(f'Returned dictionary is {dictionary}')