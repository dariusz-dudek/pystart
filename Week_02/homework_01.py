import lorem

text = lorem.text().lower().replace('\n', '')

letters = {}

for i in text:
    if not i in letters:
        letters[i] = 1
    else:
        letters[i] += 1

print(f"+{'-' * 43}+")
print(f'| {"Letter":8} | {"Occurrence":12} | {"Occurrence in %":15} |')
print(f"+{'-' * 43}+")

for ite, val in sorted(letters.items(), key=lambda item: item[1], reverse=True):
    print(f'| {ite:^8} | {val:^12} | {(val/len(text)) * 100:^15.2f} |')

print(f"+{'-' * 43}+")

