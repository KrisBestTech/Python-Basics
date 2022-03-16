total_annual_price = int(input())

basketball_shoes_cost = total_annual_price - (total_annual_price * 0.40)
basketball_suit_cost = basketball_shoes_cost - (basketball_shoes_cost * 0.20)
basketball_ball_cost = (basketball_suit_cost * 0.25)
basketball_accessories = (basketball_ball_cost * 0.20)

total_price_for_equipment = basketball_shoes_cost + basketball_suit_cost + basketball_ball_cost + \
                            basketball_accessories
full_price = total_price_for_equipment + total_annual_price

print(full_price)
