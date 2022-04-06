import math

type_of_flowers = str(input())
number_of_flowers = int(input())
budget = int(input())

total_price = 0
price = 0
money_left = 0

if type_of_flowers == 'Roses' or type_of_flowers == 'Dahlias' or \
        type_of_flowers == 'Tulips' or \
        type_of_flowers == 'Narcissus' or \
        type_of_flowers == 'Gladiolus':

    if type_of_flowers == 'Roses':
        price = 5
        total_price = price * number_of_flowers
        if number_of_flowers > 80:
            total_price -= total_price * 0.10

    elif type_of_flowers == 'Dahlias':
        price = 3.80
        total_price = price * number_of_flowers
        if number_of_flowers > 90:
            total_price -= total_price * 0.15

    elif type_of_flowers == 'Tulips':
        price = 2.80
        total_price = price * number_of_flowers
        if number_of_flowers > 80:
            total_price -= total_price * 0.15

    elif type_of_flowers == 'Narcissus':
        price = 3
        total_price = price * number_of_flowers
        if number_of_flowers < 120:
            total_price += total_price * 0.15

    elif type_of_flowers == 'Gladiolus':
        price = 2.50
        total_price = price * number_of_flowers
        if number_of_flowers < 80:
            total_price += total_price * 0.20

    money_left = budget - total_price

if money_left >= 0:
    print(f'Hey, you have a great garden with \
{number_of_flowers} {type_of_flowers} and {math.fabs(money_left):.2f} leva left.')

elif money_left < 0:
    print(f'Not enough money, you need {math.fabs(money_left):.2f} leva more.')
