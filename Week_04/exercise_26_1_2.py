def first_upper(names: list[str]) -> list:
    return list(map(lambda n: n.title(), names))


def sort_by_surname(names: list) -> list:
    return sorted(first_upper(names), key=lambda n: n.split(' ')[1])


def test_first_upper():
    assert first_upper(['zofia nowak', 'kryStyna kowalska', 'michał Lewandowski']) \
           == ['Zofia Nowak', 'Krystyna Kowalska', 'Michał Lewandowski']


def test_sort_by_surname():
    assert sort_by_surname(['Zofia Nowak', 'Krystyna Kowalska', 'Michał Lewandowski']) \
           == ['Krystyna Kowalska', 'Michał Lewandowski', 'Zofia Nowak']