num = int(input())

total = 0
max_number = ''
biggest_number = 0
diff = 0
current_number = 0

for i in range(num):
    current_number = int(input())

    total += current_number

    if i == 0:
        max_number = current_number            # This transforms the variable 'max_number' from str to int
    if current_number > max_number:            # This way I search for the biggest number
        max_number = current_number            # Then I track it

if max_number == total - max_number:
    print('Yes')
    print(f'Sum = {max_number}')

else:
    diff = abs(max_number - (total - max_number))
    print('No')
    print(f'Diff = {diff}')
