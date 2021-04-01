print('Enter the word and the program will check if this word is a palindrom or an anagram')
word1 = input('Enter the first word: ')
word2 = input('Enter the second word: ')


print(f'The word "{word1}" is {"" if word1.lower() == word1[::-1].lower() else "not "}a palindrom')
print(f'The word "{word2}" is {"" if word2.lower() == word2[::-1].lower() else "not "}a palindrom')


is_anagram = False
for character in word1:
    if word1.lower().count(character) == word2.lower().count(character):
        is_anagram = True
    else:
        is_anagram = False
        break

print(f'The words "{word1}" and "{word2}" are {"" if is_anagram else "not "}anagrams')


