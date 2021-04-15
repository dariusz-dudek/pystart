def even(numbers: list) -> list:
    return list(filter(lambda n: n % 2 == 0, numbers))


def sqrt_even(numbers: list) -> list:
    return even(list(map(lambda n: n ** 0.5, numbers)))


def test_even():
    assert even([16, 36, 25, 49]) == [16, 36]


def test_sqrt_even():
    assert sqrt_even([16, 36, 25, 49]) == [4, 6]
