movie_name = input()
capacity = int(input())
total_tickets = 0
tickets_standard = 0
tickets_student = 0
tickets_kid = 0
command = ''

if movie_name == 'Finish':
    command = movie_name

while command != 'Finish':
    capacity_filled = 0
    command = input()

    while command != 'End':
        if command == 'standard':
            tickets_standard += 1
            total_tickets += 1
            capacity_filled += 1

        elif command == 'student':
            tickets_student += 1
            total_tickets += 1
            capacity_filled += 1

        elif command == 'kid':
            tickets_kid += 1
            total_tickets += 1
            capacity_filled += 1

        if capacity_filled == capacity:
            command = input()
            break

        if command ==  'End':
            break


        command = input()

    print(f"{movie_name} - {(capacity_filled / capacity * 100):.2f}% full.")
    capacity_filled = 0
    if command != 'Finish':
        movie_name = input()
        capacity = int(input())
    else:
        break

student_tickets_percentage = (tickets_student / total_tickets) * 100
standard_tickets_percentage = (tickets_standard / total_tickets) * 100
kid_tickets_percentage = (tickets_kid / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percentage:.2f}% student tickets.")
print(f"{standard_tickets_percentage:.2f}% standard tickets.")
print(f"{kid_tickets_percentage:.2f}% kids tickets.")
