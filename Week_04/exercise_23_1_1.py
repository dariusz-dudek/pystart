def remove_vowels(text: str) -> str:
    return ''.join(char for char in str(text) if char not in 'aąAĄeęEĘiIoOóÓuUyY')


def test_remove_vowels():
    assert remove_vowels('Samuraj programowania') == 'Smrj prgrmwn'
    assert remove_vowels('Samuraj proGramowaniA') == 'Smrj prGrmwn'
    assert remove_vowels('') == ''
    assert remove_vowels(1234) == '1234'
