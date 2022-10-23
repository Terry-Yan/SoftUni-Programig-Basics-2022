number_of_days = int(input())

total_liters = 0
total_degrees = 0

for day in range(number_of_days):
    liters = float(input())
    degrees = float(input())

    total_liters += liters
    total_degrees = total_degrees + (degrees * liters)

average_degrees = total_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
elif 42 < average_degrees:
    print("Dilution with distilled water!")
