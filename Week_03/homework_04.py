def count_vowels(text: str) -> int:
    return sum([char in 'aąeęioóuy' for char in text])


print(count_vowels('ala'))
print(count_vowels('programowanie'))