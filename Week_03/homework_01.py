from random import randint

first = [randint(1, 10) for _ in range(10)]
second = [randint(1, 10) for _ in range(10)]


def sum_list(first_list: list, second_list: list) -> list:
    return [first_elem + second_elem for first_elem, second_elem in zip(first_list, second_list)]


print(f'The sum of list\n{first}\nand\n{second}\nis\n{sum_list(first, second)}')
