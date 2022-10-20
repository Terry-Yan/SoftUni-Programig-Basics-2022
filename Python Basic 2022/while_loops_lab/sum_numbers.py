correct_number = int(input())
current_number = int(input())
sum_numbers = 0

while sum_numbers < correct_number:
    sum_numbers += current_number

    if sum_numbers >= correct_number:
        break
    else:
        current_number = int(input())

print(sum_numbers)
