goal_money = float(input())
money_balance = float(input())
days_counter = 0
spent_counter = 0

while money_balance < goal_money and spent_counter < 5:
    action = input()
    money = float(input())
    days_counter += 1

    if action == 'save':
        money_balance += money
        spent_counter = 0

    elif action == 'spend':
        money_balance -= money
        spent_counter += 1

        if money_balance < 0:
            money_balance = 0

if spent_counter == 5:
    print("You can't save the money.")
    print(days_counter)

if money_balance >= goal_money:
    print(f"You saved the money for {days_counter} days.")