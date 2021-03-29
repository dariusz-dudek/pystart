from math import *
dollar_course_buy = 3.8507
dollar_course_sale = 3.9285
question = '\nEnter the amount you want ot exchange: '

while True:
    try:
        choice = int(input('What do you want to do.\n'
                           '1 - buy dollars\n'
                           '2 - sale dollars\n'
                           '3 - exit program'
                           '\n\nEnter your choice or press only ENTER to quit: '))
        if choice == 1:
            amount = float(input(question))
            print('\nFor {:.2f} {} You bought {:.2f} {} and got {:.2f} {} rest\n'.format(amount, 'zloty', (floor(10 * amount / dollar_course_buy)) / 10, 'dollars', amount - ((floor(10 * amount / dollar_course_buy)) / 10) * dollar_course_buy, 'zloty'))
        elif choice == 2:
            amount = float(input(question))
            print('\nYou sold {:.2f} {} for {:.2f} {}\n'.format(amount, 'dollars', amount * dollar_course_sale, 'zloty'))
        elif choice == 3:
            break
    except ValueError:
        print('Wrong answer. Try another time')
