import sys

number_of_lines = int(input())
max_number = -sys.maxsize
sum_numbers = 0

for i in range(number_of_lines):
    number = int(input())
    if number > max_number:
        max_number = number

    sum_numbers += number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {sum_numbers-max_number}")
else:
    print("No")
    sum_numbers -= max_number
    print(f"Diff = {abs(max_number-sum_numbers)}")
