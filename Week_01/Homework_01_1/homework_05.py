def is_leap_year(input_year):
    return input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0)


today = 2021

while True:
    try:
        birth_year = int(input('Enter your year of birth: '))
        if birth_year > today:
            print('I do not think so. This is the future. Try another time')
        else:
            print(
                f"You are {today - birth_year} and this year was {'leap' if is_leap_year(birth_year) else 'not leap'}")
            break

    except ValueError:
        print('Wrong answer. Try another time.')

def check_if_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

