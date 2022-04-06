day_of_the_week = str(input())
ticket_price = 0

if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or \
                                  day_of_the_week == 'Friday':
    ticket_price = 12
    print(ticket_price)

elif day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday':
    ticket_price = 14
    print(ticket_price)

elif day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    ticket_price = 16
    print(ticket_price)
