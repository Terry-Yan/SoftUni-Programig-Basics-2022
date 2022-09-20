number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegi_menus = int(input())
price_delivery = 2.50

price_chicken = number_of_chicken_menus * 10.35
price_fish = number_of_fish_menus * 12.40
price_vegi = number_of_vegi_menus * 8.15
price_menus = price_chicken + price_fish + price_vegi
price_desert = price_menus * 0.20
total_price = price_menus + price_desert + price_delivery

print(total_price)
