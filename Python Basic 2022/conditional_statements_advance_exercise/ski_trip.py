days = int(input()) - 1
facility = input()
evaluation = input()
facility_price = 0.00

if facility == 'room for one person':
    facility_price = days * 18.00

elif facility == 'apartment':
    if 1 <= days < 10:
        facility_price = (days * 25.00) * 0.70
    elif 10 <= days <= 15:
        facility_price = (days * 25.00) * 0.65
    elif 15 < days:
        facility_price = (days * 25.00) * 0.50

elif facility == 'president apartment':
    if 1 <= days < 10:
        facility_price = (days * 35.00) * 0.90
    elif 10 <= days <= 15:
        facility_price = (days * 35.00) * 0.85
    elif 15 < days:
        facility_price = (days * 35.00) * 0.80

if evaluation == 'positive':
    facility_price = facility_price * 1.25
    print(f"{facility_price:.2f}")
elif evaluation == 'negative':
    facility_price = facility_price * 0.90
    print(f"{facility_price:.2f}")
