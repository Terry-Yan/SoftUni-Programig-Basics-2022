change = float(input())
money_left_to_give = change * 100
count_coins = 0

while money_left_to_give > 0:
    if money_left_to_give >= 200:
        money_left_to_give -= 200
    elif money_left_to_give >= 100:
        money_left_to_give -= 100
    elif money_left_to_give >= 50:
        money_left_to_give -= 50
    elif money_left_to_give >= 20:
        money_left_to_give -= 20
    elif money_left_to_give >= 10:
        money_left_to_give -= 10
    elif money_left_to_give >= 5:
        money_left_to_give -= 5
    elif money_left_to_give >= 2:
        money_left_to_give -= 2
    elif money_left_to_give >= 1:
        money_left_to_give -= 1
    else:
        break

    count_coins += 1

print(count_coins)
