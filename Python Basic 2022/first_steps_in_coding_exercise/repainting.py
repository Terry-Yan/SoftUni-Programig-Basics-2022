square_meters_nailon = int(input())
liters_paint = int(input())
liters_thiner = int(input())
hours_work = int(input())

price_nailon = (square_meters_nailon + 2) * 1.50
price_paint = (liters_paint + (liters_paint * 0.1)) * 14.50
price_thiner = liters_thiner * 5.00
price_bags = 0.40
price_materials = price_nailon + price_paint + price_thiner + price_bags
price_work = (price_materials * 0.30) * hours_work
price_total = price_materials + price_work

print(price_total)
