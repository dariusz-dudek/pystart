def round_two_decimal_places(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        if isinstance(value, float) or isinstance(value, int):
            return round(value, 2)
        else:
            return value

    return wrapper


def test_round_two_decimal_places():
    @round_two_decimal_places
    def function(value):
        return value

    assert function(3.567) == 3.57
    assert function(3.5000) == 3.5
