steps_goal = 10000
steps_walked = 0
goal_reached = False

while True:
    new_steps = input()

    if new_steps == 'Going home':
        new_steps = input()
        steps_walked += int(new_steps)

        if steps_walked < steps_goal:
            break
    else:
        steps_walked += int(new_steps)

    if steps_walked >= steps_goal:
        goal_reached = True
        break

if goal_reached:
    steps_extra = steps_walked - steps_goal
    print("Goal reached! Good job!")
    print(f"{steps_extra} steps over the goal!")
else:
    steps_less = steps_goal - steps_walked
    print(f"{steps_less} more steps to reach goal.")
