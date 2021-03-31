print('The program will check the common characters of two words.')
first_word = set(input('Enter first word: ').lower())
second_word = set(input('Enter second word: ').lower())
print(f'Common characters in both words: {", ".join(character for character in (first_word ^ second_word))}')