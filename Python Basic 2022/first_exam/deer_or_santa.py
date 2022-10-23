import math

number_of_days = int(input())
food_in_kilograms = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())

first_deer_total_food = number_of_days * first_deer_food_per_day
second_deer_total_food = number_of_days * second_deer_food_per_day
third_deer_total_food = number_of_days * third_deer_food_per_day

total_food_needed = first_deer_total_food + second_deer_total_food + third_deer_total_food

food_diff = abs(float(food_in_kilograms) - total_food_needed)

if food_in_kilograms >= total_food_needed:
    print(f"{math.floor(food_diff)} kilos of food left.")
else:
    print(f"{math.ceil(food_diff)} more kilos of food are needed.")
