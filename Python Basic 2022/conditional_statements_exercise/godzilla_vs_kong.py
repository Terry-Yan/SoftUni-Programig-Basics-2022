film_budget = float(input())
number_of_extras = int(input())
price_of_costume = float(input())

price_of_decore = film_budget * 0.10
total_price_of_costumes = 0.00
price_of_costumes = number_of_extras * price_of_costume
discount = price_of_costumes * 0.10

if number_of_extras > 150:
    total_price_of_costumes = price_of_costumes - discount
else:
    total_price_of_costumes = number_of_extras * price_of_costume

price_total = price_of_decore + total_price_of_costumes

if price_total <= film_budget:
    print('Action!')
    money_leftover = film_budget - price_total
    print(f'Wingard starts filming with {money_leftover:.2f} leva left.')
else:
    print('Not enough money!')
    money_missing = abs(film_budget - price_total)
    print(f'Wingard needs {money_missing:.2f} leva more.')
