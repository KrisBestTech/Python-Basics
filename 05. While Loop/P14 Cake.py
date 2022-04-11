width_of_the_room = int(input())
length_of_the_room = int(input())
height_of_the_room = int(input())

total_free_cubical_metres = width_of_the_room * length_of_the_room * height_of_the_room
boxes = ''
total_room_for_boxes = 0
room_left = 0
boxes_int = 0
room_needed = 0

while total_room_for_boxes < total_free_cubical_metres:

    boxes = input()

    if boxes == 'Done':
        room_left = total_free_cubical_metres - total_room_for_boxes
        print(f'{room_left} Cubic meters left.')
        break

    total_room_for_boxes += int(boxes)

    if total_room_for_boxes > total_free_cubical_metres:
        room_needed = total_free_cubical_metres - total_room_for_boxes
        print(f'No more free space! You need {abs(room_needed)} Cubic meters more.')
        break
