import math

record_in_seconds = float(input())
pool_length = float(input())
time_for_swimming_one_meter = float(input())

water_resistance_time = pool_length // 15 * 12.5
time_without_water_resistance = pool_length * time_for_swimming_one_meter
total_time = water_resistance_time + time_without_water_resistance
exceeded_seconds = total_time - record_in_seconds

if total_time < record_in_seconds:
    water_resistance_time = math.floor(water_resistance_time)
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')

else:
    water_resistance_time = math.floor(water_resistance_time)
    print(f'No, he failed! He was {exceeded_seconds:.2f} seconds slower.')
