name = input()

count = 1
grade_final = 0
count_fail = 0
while count <= 12:
    if count_fail > 1:
        break

    grade_yearly = float(input())

    if grade_yearly < 4:
        count_fail += 1
        continue

    grade_final = grade_final + grade_yearly

    count += 1

if count_fail > 1:
    print(f'{name} has been excluded at {count} grade')
else:
    grade_average = grade_final / 12
    print(f'{name} graduated. Average grade: {grade_average:.2f}')

