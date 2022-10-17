budget = float(input())
season = input()
balance = 0.00
location = ''
facility = ''

if budget <= 100:
    location = 'Bulgaria'
    if season == 'summer':
        balance = budget * 0.30
        facility = 'Camp'
    elif season == 'winter':
        balance = budget * 0.70
        facility = 'Hotel'

elif 100 < budget <= 1000:
    location = 'Balkans'
    if season == 'summer':
        balance = budget * 0.40
        facility = 'Camp'
    elif season == 'winter':
        balance = budget * 0.80
        facility = 'Hotel'

elif budget > 1000:
    location = 'Europe'
    balance = budget * 0.90
    facility = 'Hotel'

print(f"Somewhere in {location}")
print(f"{facility} - {balance:.2f}")
