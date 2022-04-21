command = input()
sum_of_prime = 0
sum_of_non_prime = 0
while command != 'stop':
    number_entered = int(command)
    if number_entered < 0:
        print('Number is negative.')
    else:
        is_prime = True
        for number in range(2, number_entered):
            if number_entered % number == 0:
                is_prime = False
                break
        if is_prime:
            sum_of_prime += number_entered
        else:
            sum_of_non_prime += number_entered

    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime}")
