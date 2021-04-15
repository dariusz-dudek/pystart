def group_them(**kwargs):
    return '\n '.join(f'{key.capitalize()} is {value}' for key, value in kwargs.items())


def test_grup_them():
    assert group_them(wall='red', tomato='red', light='yellow', lemon='yellow', grass='green') == \
           'Wall is red\n Tomato is red\n Light is yellow\n Lemon is yellow\n Grass is green'
