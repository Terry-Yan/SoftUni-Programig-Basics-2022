budget = float(input())
graphic_cards = int(input())
processors = int(input())
ram = int(input())

price_graphic_cards = graphic_cards * 250.00
price_processors = (price_graphic_cards * 0.35) * processors
price_ram = (price_graphic_cards * 0.10) * ram
price_purchase = price_graphic_cards + price_processors + price_ram
discount = 0.0

if graphic_cards > processors:
    discount = price_purchase * 0.15

price_total = price_purchase - discount

if budget >= price_total:
    money_leftover = budget - price_total
    print(f'You have {money_leftover:.2f} leva left!')
else:
    money_leftover = price_total - budget
    print(f'Not enough money! You need {abs(money_leftover):.2f} leva more!')
