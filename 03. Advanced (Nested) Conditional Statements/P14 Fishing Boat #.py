import math

budget = int(input())
season = str(input())
number_of_fishermen = int(input())

rent_price = 0
discount1 = 0
discount2 = 0
money_left = 0
total_price = 0

if season == 'Spring' or season == 'Summer' or \
        season == 'Autumn' or \
        season == 'Winter':
    if season == 'Spring':
        rent_price = 3000

    elif season == 'Summer' or season == 'Autumn':
        rent_price = 4200

    elif season == 'Winter':
        rent_price = 2600

if number_of_fishermen <= 6:
    discount1 = rent_price * 0.10

elif 7 <= number_of_fishermen <= 11:
    discount1 = rent_price * 0.15

elif number_of_fishermen >= 12:
    discount1 = rent_price * 0.25

total_price = rent_price - discount1

if number_of_fishermen % 2 == 0 and not season == 'Autumn':
    discount2 = total_price * 0.05
    total_price = (rent_price - discount1) - discount2

money_left = budget - total_price

if money_left >= 0:
    print(f'Yes! You have {math.fabs(money_left):.2f} leva left.')

elif money_left < 0:
    print(f'Not enough money! You need {math.fabs(money_left):.2f} leva.')
