number_of_lines = int(input())
sum_left = 0
sum_right = 0

for position in range(2):
    if position == 0:
        for _ in range(number_of_lines):
            current_value = int(input())
            sum_left += current_value
    else:
        for _ in range(number_of_lines):
            current_value = int(input())
            sum_right += current_value

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    final_sum = abs(sum_left - sum_right)
    print(f"No, diff = {final_sum}")
