import math

vacation_price = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_fluffy_bears = int(input())
number_of_minions = int(input())
number_of_toy_trucks = int(input())

total_number_of_orders = number_of_puzzles + number_of_talking_dolls + number_of_fluffy_bears + \
                         number_of_minions + number_of_toy_trucks

puzzles_price = number_of_puzzles * 2.60
talking_dolls_price = number_of_talking_dolls * 3
fluffy_bears_price = number_of_fluffy_bears * 4.10
minions_price = number_of_minions * 8.20
toy_tucks_price = number_of_toy_trucks * 2

total_price = puzzles_price + talking_dolls_price + fluffy_bears_price + minions_price + toy_tucks_price

if total_number_of_orders > 50:
    total_price *= 0.75

rent = total_price * 0.10

profit = total_price - rent
money_left = profit - vacation_price

if money_left < 0:
    print(f'Not enough money! {math.fabs(money_left):.2f} lv needed.')
else:
    print(f"Yes! {math.fabs(money_left):.2f} lv left.")
