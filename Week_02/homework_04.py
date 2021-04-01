pessel = input('Enter the number and the program will check its correctness: ')

multipliers = 1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1

s = 0
for i in range(len(pessel)):
    s += int(pessel[i]) * multipliers[i]

print(f'PESSEL number {pessel} is {"" if str(s)[-1] == "0" else "is not"}correct')

day, month, year = 0, 0, 0

if int(pessel[2:4]) in range(81, 93):
    year = f'18{pessel[:2]}'
    for month_en, number in enumerate(range(81, 93)):
        if str(number) == pessel[2:4]:
            month = str(month_en)
    day = pessel[4:6]

if int(pessel[2:4]) in range(1, 13):
    year = f'19{pessel[:2]}'
    for month_en, number in enumerate(range(1, 13)):        #73021501193    06211804152
        if number == int(pessel[2:4]):
            month = month_en
    day = pessel[4:6]

if int(pessel[2:4]) in range(21, 33):
    year = f'20{pessel[:2]}'
    for month_en, number in enumerate(range(21, 33)):
        if number == int(pessel[2:4]):
            month = month_en
    day = pessel[4:6]

print(f'Day {day} month {month} year {year}')




