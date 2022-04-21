input_line = input()
sum_tickets = 0
student = 0
standard = 0
kid = 0

while input_line != 'Finish':
    name_of_movie = input_line
    availability = int(input())

    sum_tickets_movie = 0
    command_line = input()

    while command_line != 'End':
        type_of_ticket = command_line

        if type_of_ticket == 'standard':
            standard += 1

        elif type_of_ticket == 'kid':
            kid += 1

        elif type_of_ticket == 'student':
            student += 1

        sum_tickets += 1
        sum_tickets_movie += 1

        if sum_tickets_movie == availability:
            break
        command_line = input()

    availability_rate = sum_tickets_movie / availability * 100
    print(f"{name_of_movie} - {availability_rate:.2f}% full.")

    input_line = input()

print(f"Total tickets: {sum_tickets}")
sum_student = (student / sum_tickets) * 100

print(f"{sum_student:.2f}% student tickets.")
sum_standard = (standard / sum_tickets) * 100

print(f"{sum_standard:.2f}% standard tickets.")
sum_kid = (kid / sum_tickets) * 100

print(f"{sum_kid:.2f}% kids tickets.")
