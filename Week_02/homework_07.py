print('Enter two words and the program will check if they have shared characters.')

print(f'Shared characters: {", ".join(char for char in (set(input("First word: ")) & set(input("Second word: "))))}')