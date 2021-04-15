def gcd(x, y):
    return gcd(y, x % y) if y else x


def test_gcd():
    assert gcd(12, 18) == 6