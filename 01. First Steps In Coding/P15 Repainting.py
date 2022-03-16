transparent_foil = int(input()) + 2
paint_in_litres = int(input())
mixing_liquid_in_litres = int(input())
hours_to_do_work = int(input())

additional_materials = 0.40

transparent_foil_price = transparent_foil * 1.50
paint_in_litres_price = (paint_in_litres + (paint_in_litres * 0.10)) * 14.50
mixing_liquid_in_litres_price = mixing_liquid_in_litres * 5.00

total_price = transparent_foil_price + paint_in_litres_price + mixing_liquid_in_litres_price + additional_materials
cost_of_work = (total_price * 0.30) * 8

print(total_price + cost_of_work)