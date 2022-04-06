import math

figure = str(input())

if figure == 'square':
    length_of_side = float(input())
    area = length_of_side * length_of_side
    print(f'{area:.3f}')

elif figure == 'rectangle':
    length_of_side_one = float(input())
    length_of_side_two = float(input())
    area = length_of_side_one * length_of_side_two
    print(f'{area:.3f}')

elif figure == 'circle':
    radius_of_circle = float(input())
    area = math.pi * radius_of_circle * radius_of_circle
    print(f'{area:.3f}')

elif figure == 'triangle':
    length_side = float(input())
    height_side = float(input())
    area = (length_side * height_side) / 2
    print(f'{area:.3f}')