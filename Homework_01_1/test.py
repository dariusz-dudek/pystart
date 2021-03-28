def checkio(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    # replace this for solution
    a = set(data)
    b = list(a)

    return [i for i in data if not i in b or b.remove(i)]


print(checkio([1, 2, 3, 1, 3]))
