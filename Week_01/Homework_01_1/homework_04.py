from math import *

while True:
    try:
        x1, y1, x2, y2 = input('Enter the coordinates of the section in the x1 y1 x2 y2 format: ').split(' ')

        r = (((float(x2)-float(x1))**2 + (float(y2) - float(y1))**2)**0.5)/2
        print(f'The surface area of the wheel with coordinates A = ({(float(x1) + float(x2))/2},{(float(y1) + float(y2))/2}) and radius r = {round(r, 2)} is {round(pi * r ** 2, 2)}')
        print(f'A rectangle with a diagonal in points A = ({float(x1)}, {float(y1)}) B = ({float(x2)}, {float(y2)}) has an area equal to {abs(float(x1) - float(x2)) * abs(float(y1) - float(y2))}')
        break
    except ValueError:
        print('Wrong answer. Try another time')