number_of_pen_packs = int(input())
number_of_marker_packs = int(input())
liters_of_cleaner = int(input())
percentage_of_discount = int(input())/100

total_price_without_discount = number_of_pen_packs * 5.80 + number_of_marker_packs * 7.20 + liters_of_cleaner * 1.20
total_price_with_discount = total_price_without_discount - (total_price_without_discount * percentage_of_discount)

print(total_price_with_discount)
