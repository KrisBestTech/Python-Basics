name_of_actor = str(input())
points_given_by_academy = float(input())
number_of_judges = int(input())
name_of_judge = ''
points_given_by_judge = 0
points_with_academy = points_given_by_academy
points_needed = 0
points_and_judge_points = 0

if 2.0 <= points_given_by_academy <= 450.5:

    if 1 <= number_of_judges <= 20:

        for i in range(number_of_judges):
            name_of_judge = str(input())
            points_given_by_judge = float(input())

            points_with_academy += (len(name_of_judge) * points_given_by_judge) / 2

            if points_with_academy > 1250.5:
                print(
                    f'Congratulations, {name_of_actor} got a nominee for leading role with {points_with_academy:.1f}!')
                break

            else:
                continue

        if points_with_academy < 1250.5:
            points_needed = 1250.5 - points_with_academy
            print(f'Sorry, {name_of_actor} you need {abs(points_needed)} more!')
