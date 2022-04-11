input_line = input()

total_money = 0
diff = 0
deposit_money = 0

deposit = 0


while input_line != 'NoMoreMoney':

    amount = float(input_line)

    if amount >= 0:

        print(f'Increase: {amount:.2f}')

    else:
        print(f'Invalid operation!')
        break

    deposit_money += amount

    input_line = input()

total_money = deposit_money

print(f'Total: {total_money:.2f}')
