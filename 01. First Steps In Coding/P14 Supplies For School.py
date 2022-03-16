pen_pack = int(input())
markers_pack = int(input())
litres_cleaning_fluid = int(input())
discount_percentage = int(input()) / 100

pen_price = pen_pack * 5.80
markers_price = markers_pack * 7.20
cleaning_fluid_price = litres_cleaning_fluid * 1.20

total = (pen_price + markers_price + cleaning_fluid_price)
total_with_discount = total - (total * discount_percentage)

print(total_with_discount)