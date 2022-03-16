chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegetarian_menu_price = vegetarian_menu * 8.15

desert_price = (chicken_menu_price + fish_menu_price + vegetarian_menu_price) * 0.20
cost_of_delivery = 2.50

total = chicken_menu_price + fish_menu_price + vegetarian_menu_price + desert_price + cost_of_delivery

print(total)