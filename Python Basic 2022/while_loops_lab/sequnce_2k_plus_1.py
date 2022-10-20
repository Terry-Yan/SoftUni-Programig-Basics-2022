entry_number = int(input())
current_number = 1
temp_number = current_number

while current_number <= entry_number:
    print(temp_number)
    temp_number = (current_number * 2) + 1
    current_number = temp_number
