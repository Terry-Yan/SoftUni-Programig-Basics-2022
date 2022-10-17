month = input()
number_of_nights = int(input())
price_for_studio = 0.00
price_for_apartment = 0.00

if month in ['May', 'October']:
    if 7 < number_of_nights <= 14:
        price_for_studio = 50.00 * 0.95
        price_for_apartment = 65.00
    elif number_of_nights > 14:
        price_for_studio = 50.00 * 0.70
        price_for_apartment = 65.00 * 0.90
    else:
        price_for_studio = 50.00
        price_for_apartment = 65.00

elif month in ['June', 'September']:
    if number_of_nights > 14:
        price_for_studio = 75.20 * 0.80
        price_for_apartment = 68.70 * 0.90
    else:
        price_for_studio = 75.20
        price_for_apartment = 68.70

elif month in ['July', 'August']:
    if number_of_nights > 14:
        price_for_studio = 76.00
        price_for_apartment = 77.00 * 0.90
    else:
        price_for_studio = 76.00
        price_for_apartment = 77.00

total_price_apartment = price_for_apartment * number_of_nights
total_price_studio = price_for_studio * number_of_nights

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
