type_of_flowers = input()
flowers_quantity = int(input())
budget = int(input())
purchase_price = 0.00
balance = 0.00

if type_of_flowers == 'Roses':
    if flowers_quantity > 80:
        purchase_price = (flowers_quantity * 5) * 0.90
    else:
        purchase_price = flowers_quantity * 5

elif type_of_flowers == 'Dahlias':
    if flowers_quantity > 90:
        purchase_price = (flowers_quantity * 3.80) * 0.85
    else:
        purchase_price = flowers_quantity * 3.80

elif type_of_flowers == 'Tulips':
    if flowers_quantity > 80:
        purchase_price = (flowers_quantity * 2.80) * 0.85
    else:
        purchase_price = flowers_quantity * 2.80

elif type_of_flowers == 'Narcissus':
    if flowers_quantity < 120:
        purchase_price = (flowers_quantity * 3.00) * 1.15
    else:
        purchase_price = flowers_quantity * 3.00

elif type_of_flowers == 'Gladiolus':
    if flowers_quantity < 80:
        purchase_price = (flowers_quantity * 2.50) * 1.20
    else:
        purchase_price = flowers_quantity * 2.50

balance = budget - purchase_price

if balance >= 0:
    print(f"Hey, you have a great garden with {flowers_quantity} {type_of_flowers} and {balance:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(balance):.2f} leva more.")
