dictionary = {
    'zmienna': 'variable',
    'stała': 'constant',
    'wartość': 'value',
    'nawias': 'bracket',
    'przecinek': 'coma',
    'kropka': 'dot',
    'pętla': 'loop',
    'słownik': 'dictionary',
}
while True:
    choice = input('Choice dictionary:\n'
                   'e). english -> polish \n'
                   'p). polish -> english\n'
                   'q). quit program\n')
    if choice.lower() == 'e':
        while True:
            word = input('Enter the word you want to translate or press ENTER to menu: ')
            if word == '':
                break
            for key, value in dictionary.items():
                if word == value:
                    print(f'The word {word} in polish is {key}')
                    break
    if choice.lower() == 'p':
        while True:
            word = input('Enter the word you want to translate or press ENTER to menu: ')
            if word == '':
                break
            print(f'The word {word} in polish is {dictionary[word]}')