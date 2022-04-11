book_name = input()

count = 0

is_book_found = False

book_input = input()

while book_input != 'No More Books':

    if book_input == book_name:
        is_book_found = True
        print(f'You checked {count} books and found it.')
        break

    count += 1
    book_input = input()

if not is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')
