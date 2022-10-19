number_of_lines = int(input())
sum_odd = 0
sum_even = 0

for num in range(1, number_of_lines + 1):
    if num % 2 == 0:
        current_value = int(input())
        sum_odd += current_value
    else:
        current_value = int(input())
        sum_even += current_value

if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    diff = abs(sum_even - sum_odd)
    print("No")
    print(f"Diff = {diff}")
