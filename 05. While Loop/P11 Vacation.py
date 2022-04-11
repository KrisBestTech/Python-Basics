daily_goal = 10000

steps_for_the_day = 0
steps_for_the_day_in_numbers = 0
total_steps = 0

steps_over = 0
steps_under = 0

while total_steps < daily_goal:

    steps_for_the_day = input()

    if steps_for_the_day == 'Going home':
        steps_for_the_day = input()
        steps_for_the_day_in_numbers = int(steps_for_the_day)
        total_steps += steps_for_the_day_in_numbers
        break

    steps_for_the_day_in_numbers = int(steps_for_the_day)
    total_steps += steps_for_the_day_in_numbers

steps_over = total_steps - daily_goal
steps_under = daily_goal - total_steps

if steps_over >= 0 or total_steps >= daily_goal:
    print('Goal reached! Good job!')
    print(f'{steps_over} steps over the goal!')

elif steps_under >= 0:
    print(f'{steps_under} more steps to reach goal.')
