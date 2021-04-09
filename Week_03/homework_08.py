def fibonacci(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


for j in range(20):
    print(f'{j} - {fibonacci(j)}')
