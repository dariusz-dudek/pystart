def calculate_common_divisor(first, second, minim=0):
    return sorted([i for i in range(2, min(first, second) + 1) if first % i == 0 and second % i == 0 and i > minim])


print(calculate_common_divisor(3, 6))
print(calculate_common_divisor(3, 6, 4))
print(calculate_common_divisor(16, 8))