def cut(fro, to):
    def wrapper(function):
        def inner_wrapper(*args, **kwargs):
            return function(*args, **kwargs)[fro:to]

        return inner_wrapper

    return wrapper


def test_cut():
    @cut(1, 10)
    def function(value):
        return value

    assert function([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert function([0, 1, 2, 3, 4]) == [1, 2, 3, 4]
    assert function([]) == []

