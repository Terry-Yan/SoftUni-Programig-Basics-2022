number = int(input())
number_string = str(number)
number_length = len(number_string)

for i in range(1111, 10000):
    i_string = str(i)
    i_string_length = len(i_string)

    counter = 0
    for position in range(i_string_length):
        if int(i_string[position]) == 0:
            continue

        if number % int(i_string[position]) == 0:
            counter += 1

    if counter == i_string_length:
        print(i, end=' ')
