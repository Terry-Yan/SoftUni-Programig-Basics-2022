weight = float(input())
service_type = input()
distance = int(input())
total_price = 0
normal_price = 0

if service_type == 'standard':
    if 0 < weight < 1:
        normal_price = distance * 0.03
    elif 1 <= weight < 10:
        normal_price = distance * 0.05
    elif 10 <= weight < 40:
        normal_price = distance * 0.10
    elif 40 <= weight < 90:
        normal_price = distance * 0.15
    elif 90 <= weight < 150:
        normal_price = distance * 0.20

    total_price = normal_price

if service_type == 'express':
    if 0 < weight < 1:
        normal_price = distance * 0.03
        markup_per_kilo = (0.03 * 80) / 100
        markup_per_km = weight * markup_per_kilo
        markup_price = distance * markup_per_km
        total_price = normal_price + markup_price

    elif 1 <= weight < 10:
        normal_price = distance * 0.05
        markup_per_kilo = (0.05 * 40) / 100
        markup_per_km = weight * markup_per_kilo
        markup_price = distance * markup_per_km
        total_price = normal_price + markup_price

    elif 10 <= weight < 40:
        normal_price = distance * 0.10
        markup_per_kilo = (0.10 * 5) / 100
        markup_per_km = weight * markup_per_kilo
        markup_price = distance * markup_per_km
        total_price = normal_price + markup_price

    elif 40 <= weight < 90:
        normal_price = distance * 0.15
        markup_per_kilo = (0.15 * 2) / 100
        markup_per_km = weight * markup_per_kilo
        markup_price = distance * markup_per_km
        total_price = normal_price + markup_price

    elif 90 <= weight < 150:
        normal_price = distance * 0.20
        markup_per_kilo = (0.20 * 1) / 100
        markup_per_km = weight * markup_per_kilo
        markup_price = distance * markup_per_km
        total_price = normal_price + markup_price

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")
