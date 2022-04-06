import math

name_of_the_series = str(input())
length_of_episode = int(input())
length_of_break = int(input())

time_for_lunch = length_of_break * 1/8
time_to_chill = length_of_break * 1/4

total_time_for_lunch_and_chill = time_for_lunch + time_to_chill
time_left = length_of_break - total_time_for_lunch_and_chill
time_left_after_episode = time_left - length_of_episode

if time_left >= length_of_episode:
    print(f'You have enough time to watch {name_of_the_series} \
and left with {math.ceil(math.fabs(time_left_after_episode))} minutes free time.')

else:
    print(f"You don't have enough time to watch \
{name_of_the_series}, you need {math.ceil(math.fabs(time_left_after_episode))} more minutes.")
