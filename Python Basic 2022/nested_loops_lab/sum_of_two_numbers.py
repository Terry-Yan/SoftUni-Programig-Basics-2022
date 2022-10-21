starting_interval = int(input())
final_interval = int(input())
magic_number = int(input())
counter = 0
combination_flag = False

for a in range(starting_interval, final_interval + 1):
    for b in range(starting_interval, final_interval + 1):
        counter += 1

        if a + b == magic_number:
            print(f"Combination N:{counter} ({a} + {b} = {magic_number})")
            combination_flag = True
            break

    if combination_flag:
        break

if not combination_flag:
    print(f"{counter} combinations - neither equals {magic_number}")
