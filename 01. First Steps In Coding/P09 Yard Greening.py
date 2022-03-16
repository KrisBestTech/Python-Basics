square_metres = float(input())
price_sq_metres = square_metres * 7.61
discount = price_sq_metres * 0.18
final_price = price_sq_metres - discount
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')