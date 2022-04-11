import sys

input_line = input()
number = int(input_line)

max_number = -sys.maxsize

if number > max_number:

    max_number = number

while input_line != 'Stop':

    number = int(input_line)

    input_line = input()

    if number > max_number:

        max_number = number

print(max_number)
