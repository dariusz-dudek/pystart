
print('Enter ten email address ')

email_addresses = set()

for number in range(1, 11):
    if number == 1:
        email_addresses.add(input(f'Enter the {number}st email address: '))
    elif number == 2:
        email_addresses.add(input(f'Enter the {number}nd email address: '))
    elif number == 3:
        email_addresses.add(input(f'Enter the {number}rd email address: '))
    else:
        email_addresses.add(input(f'Enter the {number}th email address: '))


print(f'Entered email addresses:')
for number, address in enumerate(email_addresses, 1):
    print(f"{number} - {address}")
