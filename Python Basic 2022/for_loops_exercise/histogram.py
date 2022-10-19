number_of_lines = int(input())
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0

for num in range(number_of_lines):
    current_number = int(input())

    if 0 < current_number < 200:
        counter_1 += 1
    elif 200 <= current_number <= 399:
        counter_2 += 1
    elif 400 <= current_number <= 599:
        counter_3 += 1
    elif 600 <= current_number <= 799:
        counter_4 += 1
    elif 800 <= current_number <= 1000:
        counter_5 += 1

print(f"{(counter_1/number_of_lines) * 100:.2f}%")
print(f"{(counter_2/number_of_lines) * 100:.2f}%")
print(f"{(counter_3/number_of_lines) * 100:.2f}%")
print(f"{(counter_4/number_of_lines) * 100:.2f}%")
print(f"{(counter_5/number_of_lines) * 100:.2f}%")
