length_of_cake = int(input())
width_of_cake = int(input())

total_size = length_of_cake * width_of_cake
pieces_taken = ''
pieces_needed = 0
pieces_taken_int = 0
total_taken = 0
pieces_left = 0

while total_size > pieces_taken_int:

    pieces_taken = input()

    if pieces_taken == 'STOP':
        pieces_left = total_size - total_taken
        print(f'{pieces_left} pieces are left.')
        break

    pieces_taken_int = int(pieces_taken)
    total_taken += pieces_taken_int

    if total_taken > total_size:
        pieces_needed = total_size - total_taken
        print(f'No more cake left! You need {abs(pieces_needed)} pieces more.')
        break
