def greatest_common_divisor(first: int, second: int) -> int:
    gcd = 1
    for item in range(1, min(first, second) + 1):
        if first % item == 0 and second % item == 0:
            gcd = item
    return gcd


print(greatest_common_divisor(3, 9))
print(greatest_common_divisor(15, 25))
