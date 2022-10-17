first_number = int(input())
second_number = int(input())
operator = input()
divide_by_zero_flag = False
remnant = ''
result = 0.00

if second_number != 0:
    if operator == '+':
        result = first_number + second_number
        if result % 2 == 0:
            remnant = 'even'
        else:
            remnant = 'odd'
    elif operator == '-':
        result = first_number - second_number
        if result % 2 == 0:
            remnant = 'even'
        else:
            remnant = 'odd'
    elif operator == '*':
        result = first_number * second_number
        if result % 2 == 0:
            remnant = 'even'
        else:
            remnant = 'odd'
    elif operator == '/':
        result = first_number / second_number
    elif operator == '%':
        result = first_number % second_number
else:
    divide_by_zero_flag = True

if not divide_by_zero_flag:
    if operator in ['+', '-', '*']:
        print(f"{first_number} {operator} {second_number} = {result} - {remnant}")
    elif operator == '/':
        print(f"{first_number} / {second_number} = {result:.2f}")
    elif operator == '%':
        print(f"{first_number} % {second_number} = {result}")
else:
    print(f"Cannot divide {first_number} by zero")
