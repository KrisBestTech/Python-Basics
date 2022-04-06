lily_age = int(input())
price_for_washing_machine = float(input())
price_for_one_toy = int(input())

toys_received = 0
price_for_all_toys = 0
money_received = 0
money_saved = 0

total_sum_of_money = 0

money_diff = 0
count = 0

if 1 <= lily_age <= 77:
    if 1.00 <= price_for_washing_machine <= 10000.00:
        if 0 <= price_for_one_toy <= 40:

            for i in range(1, lily_age + 1):

                if i % 2 != 0:
                    toys_received += 1

                else:
                    money_received += 10
                    money_saved += money_received - 1

            price_for_all_toys = toys_received * price_for_one_toy
            total_sum_of_money = money_saved + price_for_all_toys

            money_diff = price_for_washing_machine - total_sum_of_money

            if total_sum_of_money >= price_for_washing_machine:
                print(f'Yes! {abs(money_diff):.2f}')

            else:
                print(f'No! {abs(money_diff):.2f}')
