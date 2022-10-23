number = int(input())
number_string = str(number)

for num1 in range(1, int(number_string[2]) + 1):
    for num2 in range(1, int(number_string[1]) + 1):
        for num3 in range(1, int(number_string[0]) + 1):
            if num1 <= 0 or num2 <= 0 or num3 <= 0:
                continue
            print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3};")

