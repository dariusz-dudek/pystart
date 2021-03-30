def frequency_sort(items):
    new = []
    for i in items:
        new.append(i)
        temp = i
        del i
        for j in items:
            if temp == j:
                new.append(j)
                del j
                break

    # for i in range(len(items)):
    #     for j in range(len(items)):
    #         if items[i] == items[j] and not i == j:
    #             items.insert(items[j], i + 1)
    #             del items[j + 1]
    #             break
    return new



print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) # [4, 4, 4, 4, 6, 6, 2, 2]