# def is_prime(number):
#     if number < 2 or number is not int:
#         return False
#     for num in range(2, int(number ** 0.5) + 1):
#         if number % num == 0:
#             return False
#     return True
from math import floor, sqrt


def is_prime(number):
    if number < 2 or number is not int:
        return False
    for div in range(2, floor(sqrt(number)) + 1):
        if number % div == 0:
            return False
    return True

print(is_prime(0))
print(is_prime(1))
print(is_prime(1.5))
