length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage_taken = float(input()) / 100

volume = length_in_cm * width_in_cm * height_in_cm
volume_in_litres = volume / 1000    # Or I can use volume * 0.001

litres_capacity = volume_in_litres * (1 - percentage_taken)
print(litres_capacity)