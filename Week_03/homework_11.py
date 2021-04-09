def count_letters(text: str, start: str = '(', end: str = ')') -> int:
    counter = 0
    for i in range(len(text)):
        if text[i] == start and not text[i + 1] == end:
            counter += len(text[i + 1: text.find(end, i + 1)])
    return counter


print(count_letters('(ala) ma (kota)'))  # 3 + 4 = 7
print(count_letters('<> kod <103>', '<', '>'))  # 0 + 3 = 3
print(count_letters('abrakadabra'))  # 0
