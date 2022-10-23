money_goal = int(input())
money_made = 0
goal_reached = False

while True:
    action = input()

    if action == 'closed':
        break

    elif action == 'haircut':
        haircut_type = input()

        if haircut_type == 'mens':
            money_made += 15
        elif haircut_type == 'ladies':
            money_made += 20
        elif haircut_type == 'kids':
            money_made += 10

    elif action == 'color':
        color_type = input()

        if color_type == 'touch up':
            money_made += 20
        elif color_type == 'full color':
            money_made += 30

    if money_made >= money_goal:
        goal_reached = True
        break

if goal_reached:
    print("You have reached your target for the day!")
else:
    diff = money_goal - money_made
    print(f"Target not reached! You need {diff}lv. more.")
print(f"Earned money: {money_made}lv.")
