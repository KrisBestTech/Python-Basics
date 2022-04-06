import math

first_finish = int(input())
second_finish = int(input())
third_finish = int(input())

total_time_in_seconds = first_finish + second_finish + third_finish
time_in_minutes = total_time_in_seconds // 60
residue_seconds = total_time_in_seconds % 60
time_in_minutes = math.floor(time_in_minutes)

if residue_seconds < 10:
    print(f'{time_in_minutes}:0{residue_seconds}')
else:
    print(f'{time_in_minutes}:{residue_seconds}')