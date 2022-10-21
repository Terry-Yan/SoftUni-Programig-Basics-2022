first_number = int(input())
second_number = int(input())
number = first_number
even_sum = 0
odd_sum = 0

while number <= second_number:
    for position in range(1, 7):
        string_number = str(number)
        if position % 2 == 0:
            even_sum += int(string_number[position - 1])
        elif position % 2 != 0:
            odd_sum += int(string_number[position - 1])

    if odd_sum == even_sum:
        print(number, end=' ')
    number += 1
    odd_sum = 0
    even_sum = 0
