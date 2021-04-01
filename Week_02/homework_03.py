text = input('Enter the text to encryption: ')
places = int(input('As far as places, I have to move the letter in the alphabet? '))

encryption = ''

for i in text:
    if not i.isalpha():
        encryption += i
    elif i.islower():
        encryption += chr((ord(i) + places - 97) % 26 + 97)
    else:
        encryption += chr((ord(i) + places - 65) % 26 + 65)

print(f'Coded text:\n{encryption}')