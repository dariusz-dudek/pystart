day_schedule = {'Incentive': 23400, 'Lunch time': 43200, 'Time to sleep': 81000}

print(f"+{'-' * 69}+")
print('| {:14} | {:30} | {:17} |'.format('Day schedule', 'Information from the program', 'What time is it'))
print(f"+{'-' * 69}+")

for key, value in day_schedule.items():
    print('| {:14} | {:^30} | {:^17} |'.format(key, value, '{:0>2d}:{:0>2d}:{:0>2d}'.format(value // 3600, (value % 3600) // 60, value % 60)))

print(f"+{'-' * 69}+")
