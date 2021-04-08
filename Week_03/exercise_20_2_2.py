def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    if count_odd and count_even:
        return len(numbers)
    if not count_odd and not count_even:
        return 0
    if count_odd:
        return len([number for number in numbers if not number % 2 == 0])
    if count_even:
        return len([number for number in numbers if number % 2 == 0])


print(f'All:................. {count_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])}')
print(f'Odd:................. {count_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], count_even=False)}')
print(f'Even:................ {count_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], count_odd=False)}')
print(f'Not even and not odd: {count_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], count_odd=False, count_even=False)}')

