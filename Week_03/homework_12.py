
def section(a: tuple[int, int], b: tuple[int, int]):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


print(section((0, 0), (10, 0)))
print(section((0, 0), (0, 10)))
print(section((0, 0), (10, 10)))
print(section((0, 0), (-10, -10)))
