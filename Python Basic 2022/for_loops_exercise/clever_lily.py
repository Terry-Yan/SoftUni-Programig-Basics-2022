lily_age = int(input())
price_of_laundry_machine = float(input())
toy_price = int(input())
savings = 0.00
money_gift = 0.00
money_gift_total = 0.00
money_toys = 0
toy_counter = 0

for i in range(1, lily_age+1):
    if i % 2 == 0:
        money_gift += 10
        money_gift_total += money_gift - 1
    else:
        toy_counter += 1

money_toys = toy_counter * toy_price
savings = money_gift_total + money_toys

if savings >= price_of_laundry_machine:
    left_over = savings - price_of_laundry_machine
    print(f"Yes! {left_over:.2f}")
else:
    diff = abs(savings - price_of_laundry_machine)
    print(f"No! {diff:.2f}")
