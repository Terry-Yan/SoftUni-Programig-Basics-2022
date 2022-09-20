square_meters_for_landscaping = float(input())
price_for_landscaping = square_meters_for_landscaping * 7.61
discount = price_for_landscaping * 0.18
total_price_for_landscaping = price_for_landscaping - discount

print(f'The final price is: {total_price_for_landscaping} lv.')
print(f'The discount is: {discount} lv.')
