def decimal_to_binary(number: int):
    a = ''
    while number >= 1:
        a += str(number % 2)
        number = number // 2
    return int(''.join(a[j] for j in range(len(a) - 1, -1, -1)))
