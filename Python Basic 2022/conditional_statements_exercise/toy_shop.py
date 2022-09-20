price_vacation = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

money_purchase = number_of_puzzles * 2.60 + number_of_dolls * 3 + \
               number_of_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks * 2

number_of_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
money_earned = 0.00

if number_of_toys >= 50:
    money_earned = money_purchase - (money_purchase * 0.25)
else:
    money_earned = money_purchase

money_left = money_earned - (money_earned * 0.1)

if money_left >= price_vacation:
    money_final = money_left - price_vacation
    print(f'Yes! {money_final:.2f} lv left.')
else:
    money_missing = abs(money_left - price_vacation)
    print(f'Not enough money! {money_missing:.2f} lv needed.')
