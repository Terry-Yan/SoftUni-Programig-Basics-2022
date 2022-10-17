product = input()
city = input()
quantity = float(input())

price_of_item = 0.00

if city == 'Sofia':
    if product == 'coffee':
        price_of_item = 0.50
    elif product == 'water':
        price_of_item = 0.80
    elif product == 'beer':
        price_of_item = 1.20
    elif product == 'sweets':
        price_of_item = 1.45
    elif product == 'peanuts':
        price_of_item = 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        price_of_item = 0.40
    elif product == 'water':
        price_of_item = 0.70
    elif product == 'beer':
        price_of_item = 1.15
    elif product == 'sweets':
        price_of_item = 1.30
    elif product == 'peanuts':
        price_of_item = 1.50
elif city == 'Varna':
    if product == 'coffee':
        price_of_item = 0.45
    elif product == 'water':
        price_of_item = 0.70
    elif product == 'beer':
        price_of_item = 1.10
    elif product == 'sweets':
        price_of_item = 1.35
    elif product == 'peanuts':
        price_of_item = 1.55

total_price = price_of_item * quantity
print(total_price)
