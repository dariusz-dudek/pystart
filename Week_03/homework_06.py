import lorem


def words_len(text: str) -> list:
    return [word for word in text if 4 < len(word) < 8]


sample_text = lorem.paragraph().lower().replace('\n', '').replace('.', '').split(' ')

print(f'Words I Healthy than 4 and shorter than 8 characters:  {", ".join(words_len(sample_text))}')
