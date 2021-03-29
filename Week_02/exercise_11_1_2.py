password = input('Enter the password and program will change every \'a\' to \'@\' and every \'s\' to \'$\': ')
new_password = str()

for letter in password:
    if letter == 'a':
        new_password += '@'
    elif letter == 's':
        new_password += '$'
    else:
        new_password += letter

print(f'Your changed password is {new_password}')