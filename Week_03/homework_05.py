def even_numbers(numbers: list) -> list:
    return [number for number in numbers if number % 2 == 0]


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
