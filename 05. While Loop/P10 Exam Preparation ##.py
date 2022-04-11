money_needed_for_vacation = float(input())
money_saved = float(input())

days_counter = 0
spend_counter = 0

while money_saved < money_needed_for_vacation and spend_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1

    if command == 'save':
        money_saved += money
        spend_counter = 0

    elif command == 'spend':
        money_saved -= money
        spend_counter += 1
        if money_saved < 0:
            money_saved = 0

if spend_counter == 5:
    print(f'You can\'t save the money.')
    print(days_counter)

if money_saved >= money_needed_for_vacation:
    print(f'You saved the money for {days_counter} days.')
