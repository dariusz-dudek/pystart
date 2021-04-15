def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def sum_fibonacci(n):
    return sum([fibonacci(i) for i in range(n + 1)])


def test_sum_fibonacci():
    assert sum_fibonacci(10) == 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55


def test_fibonacci():
    assert fibonacci(10) == 55
