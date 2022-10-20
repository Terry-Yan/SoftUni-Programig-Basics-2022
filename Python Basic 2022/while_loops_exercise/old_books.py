book_title = input()
title = input()
book_count = 0
is_found = False

while title != 'No More Books':
    if title == book_title:
        is_found = True
        break
    else:
        title = input()

    book_count += 1

if is_found:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
