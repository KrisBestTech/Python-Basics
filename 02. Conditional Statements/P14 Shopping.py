import math

budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = video_cards * 250

percentage_of_video_cards_price_ram = video_cards_price * 0.10
percentage_of_video_cards_price_processors = video_cards_price * 0.35

processors_price = processors * percentage_of_video_cards_price_processors
ram_memory_price = ram_memory * percentage_of_video_cards_price_ram

total_price = video_cards_price + processors_price + ram_memory_price
money_left = budget - total_price

if video_cards > processors:
    total_price = total_price - (total_price * 0.15)
    money_left = budget - total_price

if total_price <= budget:
    print(f'You have {math.fabs(money_left):.2f} leva left!')
else:
    print(f'Not enough money! You need {math.fabs(money_left):.2f} leva more!')
