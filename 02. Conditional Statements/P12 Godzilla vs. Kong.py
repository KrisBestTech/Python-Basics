import math

budget_of_the_movie = float(input())
number_of_extras = int(input())
price_of_clothing_for_one_extra = float(input())

price_for_decor = budget_of_the_movie * 0.10
price_for_clothing = number_of_extras * price_of_clothing_for_one_extra

if number_of_extras > 150:
    price_for_clothing = price_for_clothing - (price_for_clothing * 0.10)

money_for_decor_and_clothes = price_for_clothing + price_for_decor
money = budget_of_the_movie - money_for_decor_and_clothes

if money_for_decor_and_clothes > budget_of_the_movie:
    print(f'Not enough money!')
    print(f'Wingard needs {math.fabs(money):.2f} leva more.')

elif money_for_decor_and_clothes <= budget_of_the_movie:
    print(f'Action!')
    print(f'Wingard starts filming with {math.fabs(money):.2f} leva left.')
