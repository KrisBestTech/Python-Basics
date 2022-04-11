failed_tests = int(input())

failed_times = 0
has_failed = True
solved_problems = 0
grades_sum = 0
last_problem = ''

while failed_times < failed_tests:
    tasks = input()
    if tasks == 'Enough':
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems += 1
    last_problem = tasks

if has_failed:
    print(f'You need a break, {failed_tests} poor grades.')
else:
    print(f'Average score: {grades_sum / solved_problems:.2f}')
    print(f'Number of problems: {solved_problems}')
    print(f'Last problem: {last_problem}')
