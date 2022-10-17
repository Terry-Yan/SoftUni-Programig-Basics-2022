budget = int(input())
season = input()
number_of_fishermen = int(input())
ship_price = 0
balance = 0.00

if season == 'Spring':
    ship_price = 3000
    if 1 <= number_of_fishermen <= 6:
        ship_price = ship_price * 0.90
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

    elif 7 <= number_of_fishermen <= 11:
        ship_price = ship_price * 0.85
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

    elif number_of_fishermen >= 12:
        ship_price = ship_price * 0.75
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

if season == 'Summer':
    ship_price = 4200
    if 1 <= number_of_fishermen <= 6:
        ship_price = ship_price * 0.90
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

    elif 7 <= number_of_fishermen <= 11:
        ship_price = ship_price * 0.85
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

    elif number_of_fishermen >= 12:
        ship_price = ship_price * 0.75
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95


if season == 'Autumn':
    ship_price = 4200
    if 1 <= number_of_fishermen <= 6:
        ship_price = ship_price * 0.90

    elif 7 <= number_of_fishermen <= 11:
        ship_price = ship_price * 0.85

    elif number_of_fishermen >= 12:
        ship_price = ship_price * 0.75

if season == 'Winter':
    ship_price = 2600
    if 1 <= number_of_fishermen <= 6:
        ship_price = ship_price * 0.90
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

    elif 7 <= number_of_fishermen <= 11:
        ship_price = ship_price * 0.85
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

    elif number_of_fishermen >= 12:
        ship_price = ship_price * 0.75
        if number_of_fishermen % 2 == 0:
            ship_price = ship_price * 0.95

balance = budget - ship_price
if balance >= 0:
    print(f"Yes! You have {balance:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(balance):.2f} leva.")
