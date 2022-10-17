fruit = input()
day_of_week = input()
quantity = float(input())
price_of_item = 0.00

if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit == 'banana':
        price_of_item = 2.50
    if fruit == 'apple':
        price_of_item = 1.20
    if fruit == 'orange':
        price_of_item = 0.85
    if fruit == 'grapefruit':
        price_of_item = 1.45
    if fruit == 'kiwi':
        price_of_item = 2.70
    if fruit == 'pineapple':
        price_of_item = 5.50
    if fruit == 'grapes':
        price_of_item = 3.85
elif day_of_week in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        price_of_item = 2.70
    if fruit == 'apple':
        price_of_item = 1.25
    if fruit == 'orange':
        price_of_item = 0.90
    if fruit == 'grapefruit':
        price_of_item = 1.60
    if fruit == 'kiwi':
        price_of_item = 3.00
    if fruit == 'pineapple':
        price_of_item = 5.60
    if fruit == 'grapes':
        price_of_item = 4.20

total_price = price_of_item * quantity
if total_price != 0.00:
    print(f'{total_price:.2f}')
else:
    print('error')
