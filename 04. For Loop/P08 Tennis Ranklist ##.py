import math

number_of_tournaments = int(input())
initial_points = int(input())

points = 0
points_on_average = 0
total_points = 0

win_percentage = 0
win_count = 0

if 1 <= number_of_tournaments <= 20:
    if 1 <= initial_points <= 4000:

        for i in range(number_of_tournaments):
            outcome = str(input())

            if outcome == 'W' or outcome == 'F' or outcome == 'SF':

                if outcome == 'W':
                    win_count += 1
                    points += 2000

                elif outcome == 'F':
                    points += 1200

                elif outcome == 'SF':
                    points += 720

        points_on_average = points / number_of_tournaments
        total_points = initial_points + points
        win_percentage = win_count / number_of_tournaments * 100

        print(f'Final points: {total_points}')
        print(f'Average points: {math.floor(points_on_average)}')
        print(f'{win_percentage:.2f}%')
