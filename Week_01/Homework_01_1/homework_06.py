from math import *
while True:
    try:
        triangle = float(input('Enter the length of the side of the equilateral triangle: '))
        triangle_field = ((triangle ** 2) * (3 ** 0.5)) / 4
        cone_volume = (pi * (triangle / 2) * ((triangle * (3 ** 0.5))/2)) / 3

        print('The surface area of the equilateral triangle with a side {:.2f} is {:.2f}'.format(triangle, triangle_field))
        print('The volume of the cone was created by turning this triangle around the axis is {:.2f}'.format(cone_volume))
        break

    except ValueError:
        print('Wrong answer. This is not integer. Try another time.')
