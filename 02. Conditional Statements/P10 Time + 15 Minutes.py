hour_of_the_day = int(input())
minutes = int(input())
minutes += 15
hour_of_the_day += minutes // 60
minutes %= 60
if hour_of_the_day > 23:
    hour_of_the_day = 0
print(f"{hour_of_the_day}:{minutes:02d}")
