initial_number = int(input())
bonus_points = 0

if initial_number <= 100:
    bonus_points += 5
elif 100 < initial_number <= 1000:
    bonus_points = initial_number * 0.2
elif initial_number > 1000:
    bonus_points = initial_number * 0.1

additional_bonus = 0

if initial_number % 2 == 0:
    additional_bonus += 1

third_bonus = 0

if initial_number % 10 == 5:
    third_bonus += 2

all_bonuses = bonus_points + additional_bonus + third_bonus

print(f'{all_bonuses}')
print(f'{initial_number + all_bonuses}')
