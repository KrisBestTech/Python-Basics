first_number = int(input())
second_number = int(input())
operator = input()

result = int()

if operator == '/' or operator == '*' or operator == '+' \
        or operator == '-' or operator == '%':

    odd_or_even = 'odd'

    if operator == '/' and second_number != 0:
        result = first_number / second_number
        if result % 2 == 0:
            odd_or_even = 'even'

        result = first_number / second_number
        print(f'{first_number} {operator} {second_number} = {result:.2f}')

    elif operator == '*':
        result = first_number * second_number
        if result % 2 == 0:
            odd_or_even = 'even'

        print(f'{first_number} {operator} {second_number} = {result} - {odd_or_even}')

    elif operator == '+':
        result = first_number + second_number
        if result % 2 == 0:
            odd_or_even = 'even'

        print(f'{first_number} {operator} {second_number} = {result} - {odd_or_even}')

    elif operator == '-':
        result = first_number - second_number
        if result % 2 == 0:
            odd_or_even = 'even'

        print(f'{first_number} {operator} {second_number} = {result} - {odd_or_even}')

    elif operator == '%' and second_number != 0:
        result = first_number % second_number
        if result % 2 == 0:
            odd_or_even = 'even'

        print(f'{first_number} {operator} {second_number} = {result}')

    elif operator == '%' and second_number == 0:

        print(f'Cannot divide {first_number} by zero')

    elif operator == '/' and second_number == 0:

        print(f'Cannot divide {first_number} by zero')
