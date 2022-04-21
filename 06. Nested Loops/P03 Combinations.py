starting_number = int(input())
ending_number = int(input())
magic_number = int(input())

total = 0
count = 0
combination_found = False

if 1 <= starting_number <= 999:
    if starting_number < ending_number <= 1000:
        if 1 <= magic_number <= 10000:

            for num1 in range(starting_number, ending_number + 1):
                for num2 in range(starting_number, ending_number + 1):

                    total = num1 + num2
                    count += 1

                    if total == magic_number:
                        combination_found = True
                        print(f'Combination N:{count} ({num1} + {num2} = {total})')
                        break

                if combination_found:
                    break

            if not combination_found:
                print(f'{count} combinations - neither equals {magic_number}')
