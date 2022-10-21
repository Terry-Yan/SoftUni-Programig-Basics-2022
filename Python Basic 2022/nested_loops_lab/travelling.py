destination = input()
budget_goal = float(input())
budget_current = 0.00
travel_flag = True

while True:
    if not travel_flag:
        break
    else:
        while True:
            deposit = input()

            if deposit == 'End':
                travel_flag = False
                break

            budget_current += float(deposit)

            if budget_current >= budget_goal:
                print(f"Going to {destination}!")
                deposit = input()
                if deposit == 'End':
                    travel_flag = False
                    break
                else:
                    budget_current = 0.00
                    destination = deposit
                    budget_goal = float(input())
                break
