def vowel_in_sentence(text):
    return set(char for char in text.lower() if char in 'aąeęioóuy')


sentence = input('Enter your sentence and the program will display all vowels: ')

print(f'The vowels in sentence {sentence} are: {", ".join(vowel_in_sentence(sentence))}')
