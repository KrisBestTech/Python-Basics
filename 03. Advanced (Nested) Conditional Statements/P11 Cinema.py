type_of_projection = str(input())
rows = int(input())
columns = int(input())

price = 0
number_of_seats = rows * columns

if type_of_projection == 'Premiere':
    price = 12.00

elif type_of_projection == 'Normal':
    price = 7.50

elif type_of_projection == 'Discount':
    price = 5.00

total = price * number_of_seats
print(f'{total:.2f}')
