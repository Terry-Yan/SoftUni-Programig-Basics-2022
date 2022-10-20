space_width = int(input())
space_length = int(input())
space_height = int(input())

total_space = space_width * space_length * space_height
space_left = total_space
free_space_flag = False

while space_left >= 0:
    box = input()

    if box == 'Done':
        free_space_flag = True
        break
    elif box != 'Done':
        space_left -= int(box)

if free_space_flag:
    print(f"{space_left} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space_left)} Cubic meters more.")
