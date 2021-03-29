from math import fabs
print('Program oblicza pole trójkąta o podanych współrzędnych')
ax = float(input('Podaj współrzędną x punktu A: '))
ay = float(input('Podaj współrzędną y punktu A: '))
bx = float(input('Podaj współrzędną x punktu B: '))
by = float(input('Podaj współrzędną y punktu B: '))
cx = float(input('Podaj współrzędną x punktu C: '))
cy = float(input('Podaj współrzędną c punktu Y: '))

field = 0.5 * fabs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))

print(f'Pole powierzchni trójkąta o wierzchołkach')
print(f'A = ({ax}, {by})')
print(f'B = ({bx}, {by})')
print(f'C = ({cx}, {cy})')
print(f'wynosi {field}')
